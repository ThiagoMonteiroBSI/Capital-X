from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from integracoes.facta_credito.client import FactaCreditoClient
from .serializers import SimularEtapa1Serializer

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
        serializer = SimularEtapa1Serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            cliente = FactaCreditoClient()
            resultado = cliente.simular_etapa_1(dados_simulacao=serializer.validated_data)
            return Response(resultado, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"erro": True, "mensagem": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CadastrarDadosPessoaisView(APIView):
    def post(self, request):
        try:
            cliente = FactaCreditoClient()
            resultado = cliente.cadastrar_dados_pessoais(dados_pessoais=request.data)
            return Response(resultado, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": True, "mensagem": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GerarPropostaView(APIView):
    def post(self, request):
        codigo_cliente = request.data.get('codigo_cliente')
        id_simulador = request.data.get('id_simulador')
        tipo_formalizacao = request.data.get('tipo_formalizacao', 'DIG')
        
        try:
            cliente = FactaCreditoClient()
            resultado = cliente.gerar_proposta(codigo_cliente, id_simulador, tipo_formalizacao)
            return Response(resultado, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": True, "mensagem": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EnviarLinkFormalizacaoView(APIView):
    def post(self, request):
        serializer = EnviarLinkFormalizacaoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            cliente = FactaCreditoClient()
            
            codigo_af = serializer.validated_data['codigo_af']
            # Como agora o tipo_envio é garantido pelo serializer, acessamos diretamente!
            tipo_envio = serializer.validated_data['tipo_envio'] 
            
            resultado = cliente.enviar_link_formalizacao(codigo_af, tipo_envio)
            return Response(resultado, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"erro": True, "mensagem": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)