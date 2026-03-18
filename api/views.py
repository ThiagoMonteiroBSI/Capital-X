from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from integracoes.facta_credito.client import FactaCreditoClient

class OperacoesDisponiveisView(APIView):
    def get(self, request):
        cpf = request.query_params.get('cpf')
        data_nascimento = request.query_params.get('data_nascimento')
        valor_renda = request.query_params.get('valor_renda')
        
        if not all([cpf, data_nascimento, valor_renda]):
            return Response(
                {"erro": True, "mensagem": "CPF, data_nascimento e valor_renda são obrigatórios."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cliente = FactaCreditoClient()
            resultado = cliente.operacoes_disponiveis(
                cpf=cpf, 
                data_nascimento=data_nascimento, 
                valor_renda=valor_renda
            )
            return Response(resultado, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"erro": True, "mensagem": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SimularEtapa1View(APIView):
    def post(self, request):
        dados_front = request.data
        try:
            cliente = FactaCreditoClient()
            resultado = cliente.simular_etapa_1(dados_simulacao=dados_front)
            return Response(resultado, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"erro": True, "mensagem": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
