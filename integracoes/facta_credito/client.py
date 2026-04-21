import os
import requests
from requests.exceptions import RequestException, Timeout
from django.core.cache import cache

class FactaCreditoClient:
    def __init__(self):
        self.base_url = os.getenv('FACTA_URL', 'https://webservice.facta.com.br')
        self.basic_token = os.getenv('FACTA_BASIC_TOKEN')
        
        if not self.basic_token:
            raise ValueError(
                "Credencial FACTA_BASIC_TOKEN ausente! Verifique o arquivo .env."
            )
            
        self.cache_key = 'facta_token'
        self.session = requests.Session()
        self.timeout = 15

    def _gerar_token(self):
        url = f"{self.base_url}/gera-token"
        headers = {
            'Authorization': f'Basic {self.basic_token}'
        }
        
        try:
            response = self.session.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            dados = response.json()
            
            if dados.get('erro'):
                raise Exception(dados.get('mensagem', 'Erro desconhecido ao gerar token FACTA'))
                
            token = dados['token']
            cache.set(self.cache_key, token, timeout=3500)
            return token
            
        except Timeout:
            raise Exception("Timeout: A API da Facta demorou muito para responder na geração do token.")
        except RequestException as e:
            raise Exception(f"Erro de comunicação com a Facta (Token): {str(e)}")

    def get_headers(self):
        token = cache.get(self.cache_key)
        if not token:
            token = self._gerar_token()
            
        return {
            'Authorization': f'Bearer {token}'
        }

    def operacoes_disponiveis(self, cpf, data_nascimento, valor_renda):
        url = f"{self.base_url}/proposta/operacoes-disponiveis"
        headers = self.get_headers()
        
        params = {
            'produto': 'D',
            'tipo_operacao': 13,
            'averbador': 10010,
            'convenio': 3,
            'opcao_valor': 1,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'valor_renda': valor_renda
        }
        
        try:
            response = self.session.get(url, headers=headers, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"Erro ao consultar operações na Facta: {str(e)}")

    def simular_etapa_1(self, dados_simulacao):
        url = f"{self.base_url}/proposta/etapa1-simulador"
        headers = self.get_headers()
        
        payload = {
            'produto': 'D',
            'tipo_operacao': 13,
            'averbador': 10010,
            'convenio': 3,
        }
        payload.update(dados_simulacao)
        
        try:
            response = self.session.post(url, headers=headers, data=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"Erro na simulação Etapa 1: {str(e)}")

    def cadastrar_dados_pessoais(self, dados_pessoais):
        url = f"{self.base_url}/proposta/etapa2-dados-pessoais"
        headers = self.get_headers()
        
        try:
            response = self.session.post(url, headers=headers, data=dados_pessoais, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"Erro ao cadastrar dados pessoais: {str(e)}")

    def gerar_proposta(self, codigo_cliente, id_simulador, tipo_formalizacao):
        url = f"{self.base_url}/proposta/etapa3-proposta-cadastro"
        headers = self.get_headers()
        
        payload = {
            'codigo_cliente': codigo_cliente,
            'id_simulador': id_simulador,
            'tipo_formalizacao': tipo_formalizacao
        }
        
        try:
            response = self.session.post(url, headers=headers, data=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"Erro ao gerar proposta: {str(e)}")

    def enviar_link_formalizacao(self, codigo_af, tipo_envio):
        url = f"{self.base_url}/proposta/envio-link"
        headers = self.get_headers()
        
        payload = {
            'codigo_af': codigo_af,
            'tipo_envio': tipo_envio
        }
        
        try:
            response = self.session.post(url, headers=headers, data=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"Erro ao enviar link de formalização: {str(e)}")