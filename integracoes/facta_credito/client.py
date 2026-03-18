from integracoes.base_client import BaseFactaClient

class FactaCreditoClient(BaseFactaClient):

    def consultar_ofertas(self, cpf: str):
        endpoint = "/consignado-trabalhador/consulta-ofertas"
        parametros = {"cpf": cpf} 
        
        return self._fazer_requisicao("GET", endpoint, params=parametros)

    def operacoes_disponiveis(self, cpf: str, data_nascimento: str, valor_renda: float, valor_parcela: float = None, prazo: int = None):
        endpoint = "/proposta/operacoes-disponiveis"
        
        parametros = {
            "produto": "D",
            "tipo_operacao": 13,
            "averbador": 10010,
            "convenio": 3,
            "opcao_valor": 1 if valor_parcela is None else 2, 
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "valor_renda": valor_renda
        }

        if valor_parcela:
            parametros["valor_parcela"] = valor_parcela
        if prazo:
            parametros["prazo"] = prazo

        return self._fazer_requisicao("GET", endpoint, params=parametros)

    def simular_etapa_1(self, dados_simulacao: dict):
        endpoint = "/proposta/etapa1-simulador"
              
        payload = {
            "produto": "D",
            "tipo_operacao": 13,
            "averbador": 10010,
            "convenio": 3,
            "cpf": dados_simulacao.get("cpf"),
            "data_nascimento": dados_simulacao.get("data_nascimento"),  
            "login_certificado": dados_simulacao.get("login_certificado"), 
            "codigo_tabela": dados_simulacao.get("codigo_tabela"),
            "prazo": dados_simulacao.get("prazo"), 
            "valor_operacao": dados_simulacao.get("valor_operacao"), 
            "valor_parcela": dados_simulacao.get("valor_parcela"), 
            "coeficiente": dados_simulacao.get("coeficiente") 
        }
        
        if "vendedor" in dados_simulacao:
            payload["vendedor"] = dados_simulacao["vendedor"]

        return self._fazer_requisicao("POST", endpoint, data=payload)

    def cadastrar_dados_pessoais(self, dados_pessoais: dict):
        endpoint = "/proposta/etapa2-dados-pessoais"
        
        return self._fazer_requisicao("POST", endpoint, data=dados_pessoais)

    def gerar_proposta(self, codigo_cliente: str, id_simulador: str, tipo_formalizacao: str = "DIG"):
        endpoint = "/proposta/etapa3-proposta-cadastro"
        
        payload = {
            "codigo_cliente": codigo_cliente,
            "id_simulador": id_simulador,
            "tipo_formalizacao": tipo_formalizacao
        }
        
        return self._fazer_requisicao("POST", endpoint, data=payload)

    def enviar_link_formalizacao(self, codigo_af: str, tipo_envio: str = "sms"):
        endpoint = "/proposta/envio-link"
        
        payload = {
            "codigo_af": codigo_af,
            "tipo_envio": tipo_envio
        }
        
        return self._fazer_requisicao("POST", endpoint, data=payload)
