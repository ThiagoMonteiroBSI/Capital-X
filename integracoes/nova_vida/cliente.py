import os
import requests
from requests.exceptions import RequestException, Timeout
from django.core.cache import cache

class NovaVidaClient:
    def __init__(self):
        self.base_url = os.getenv('NOVA_VIDA_URL', 'https://wsnv.novavidati.com.br/wslocalizador.asmx')
        self.usuario = os.getenv('NOVA_VIDA_USUARIO')
        self.senha = os.getenv('NOVA_VIDA_SENHA')
        self.cliente = os.getenv('NOVA_VIDA_CLIENTE')
        
        # 1. Validacao de variaveis de ambiente - Thiago
        if not all([self.usuario, self.senha, self.cliente]):
            raise ValueError(
                "Credenciais da Nova Vida TI ausentes! Verifique se NOVA_VIDA_USUARIO, "
                "NOVA_VIDA_SENHA e NOVA_VIDA_CLIENTE estão preenchidas no arquivo .env."
            )
            
        self.cache_key = 'nova_vida_token'
        self.session = requests.Session()
        
        # 3. Timeout padrão de 10s -- Thigas
        self.timeout = 10 

    def _gerar_token(self):
       #Gera o token de 24 horas explicado no texto da API
        url = f"{self.base_url}/GerarTokenJson"
        
        payload = {
            "credencial": {
                "usuario": self.usuario,
                "senha": self.senha,
                "cliente": self.cliente
            }
        }
        
        try:
            response = self.session.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()           
            token = response.text.replace('"', '').strip()
            cache.set(self.cache_key, token, timeout=82800)
            return token
            
        except Timeout:
            raise Exception("Timeout: A API da Nova Vida demorou muito para responder na geração do token.")
        except RequestException as e:
            raise Exception(f"Erro de comunicação com a Nova Vida (Token): {str(e)}")

    def get_headers(self):
        token = cache.get(self.cache_key)
        if not token:
            token = self._gerar_token()
            
        return {
            'Content-Type': 'application/json',
            'Token': token
        }

    def consultar_nvcheck(self, documento: str):
        url = f"{self.base_url}/NVCHECKJson"
        
        try:
            headers = self.get_headers()
            
            payload = {
                "nvcheck": {
                    "Documento": documento
                }
            }
            
            response = self.session.post(url, headers=headers, json=payload, timeout=self.timeout)
            response.raise_for_status()
            
            return response.json()
            
        except Timeout:
            raise Exception("Timeout: A consulta NVCheck demorou mais que o esperado para retornar os dados.")
        except RequestException as e:
            raise Exception(f"Erro de comunicação com a Nova Vida (NVCheck): {str(e)}")