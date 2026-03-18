from django.urls import path
from .views import OperacoesDisponiveisView, SimularEtapa1View

urlpatterns = [
    path('operacoes-disponiveis/', OperacoesDisponiveisView.as_view(), name='operacoes-disponiveis'),
    path('simular-etapa1/', SimularEtapa1View.as_view(), name='simular-etapa1'),
]