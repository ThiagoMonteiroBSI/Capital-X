import os
import base64
import requests
from django.core.cache import cache

class BaseFactaClient:
   
    def __init__(self):
        
        self.base_url = os.getenv('FACTA_API_URL')
        self.usuario = os.getenv('FACTA_USUARIO')
        self.senha = os.getenv('FACTA_SENHA')
        

        self.cache_key = 'facta_api_token'

    def _gerar_token(self):
        
        url = f"{self.base_url.rstrip('/')}/gera-token"
        
        credenciais = f"{self.usuario}:{self.senha}"
        credenciais_b64 = base64.b64encode(credenciais.encode('utf-8')).decode('utf-8')
        
        headers = {
            'Authorization': f'Basic {credenciais_b64}'
        }

        # Faz a requisição get para pegar o token - Thiagop
        response = requests.get(url, headers=headers)
        
        response.raise_for_status()
        
        dados = response.json()
        
        if not dados.get('erro') and 'token' in dados:
            token = dados['token']
            #tempo do token de login, 55 minutos até espirar
            cache.set(self.cache_key, token, timeout=3300)
            return token
        else:
            raise Exception(f"Erro ao gerar token Facta: {dados.get('mensagem')}")

    def get_headers(self):
       
        token = cache.get(self.cache_key)
        
        if not token:
            token = self._gerar_token()
            
        return {
            'Authorization': f'Bearer {token}'
        }

    def _fazer_requisicao(self, metodo, endpoint, params=None, data=None):

        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = self.get_headers()
        
        response = requests.request(
            method=metodo,
            url=url,
            headers=headers,
            params=params,
            data=data
        )
        
        response.raise_for_status()
        return response.json()