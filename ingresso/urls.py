from django.urls import path

from ingresso.views import SolicitarIngresso
from ingresso.views import solicitarIngressoFuncao
from ingresso.views import MinhasSolicitacoes
from ingresso.views import cancelarSolicitacaoFuncao
from .views import Pdf
urlpatterns = [

    path('new/<int:pk>/', SolicitarIngresso.as_view(), name="solicitar_ingresso"),
    path('minhas-solicitacoes/', MinhasSolicitacoes.as_view(), name="minhas_solicitacoes"),
    path('cancelar-solicitacao/<int:id_ingresso>/<int:id_evento>/', cancelarSolicitacaoFuncao, name="cancelar_solicitacao"),
    path('new-funcao/<int:id_evento>/', solicitarIngressoFuncao, name="solicitar_ingresso_funcao"),
    path('gerar-ingresso/<int:id_ingresso>/', Pdf.as_view(), name="gerar_ingresso"),
    # path('new/', SolicitarIngresso.as_view(), name="solicitar_ingresso"),

]
