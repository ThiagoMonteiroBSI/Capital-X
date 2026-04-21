from django.urls import path
from .views import (
    OperacoesDisponiveisView, 
    SimularEtapa1View,
    CadastrarDadosPessoaisView,
    GerarPropostaView,
    EnviarLinkFormalizacaoView,
    ConsultarNVCheckView
)

urlpatterns = [
    path('operacoes-disponiveis/', OperacoesDisponiveisView.as_view(), name='operacoes-disponiveis'),
    path('simular-etapa1/', SimularEtapa1View.as_view(), name='simular-etapa1'),
    path('cadastrar-dados/', CadastrarDadosPessoaisView.as_view(), name='cadastrar-dados'),
    path('gerar-proposta/', GerarPropostaView.as_view(), name='gerar-proposta'),
    path('enviar-link/', EnviarLinkFormalizacaoView.as_view(), name='enviar-link'),
    path('consultar-nvcheck/', ConsultarNVCheckView.as_view(), name='consultar-nvcheck'),
]