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
            "produto": "D", # Fixo 
            "tipo_operacao": 13, # Fixo 
            "averbador": 10010, # Fixo 
            "convenio": 3, # Fixo 
            "cpf": dados_simulacao.get("cpf"), # 
            "data_nascimento": dados_simulacao.get("data_nascimento"),  
            "login_certificado": dados_simulacao.get("login_certificado"), 
            "codigo_tabela": dados_simulacao.get("codigo_tabela"), # 
            "prazo": dados_simulacao.get("prazo"), 
            "valor_operacao": dados_simulacao.get("valor_operacao"), 
            "valor_parcela": dados_simulacao.get("valor_parcela"), 
            "coeficiente": dados_simulacao.get("coeficiente") 
        }
        
        if "vendedor" in dados_simulacao:
            payload["vendedor"] = dados_simulacao["vendedor"]

        return self._fazer_requisicao("POST", endpoint, data=payload)