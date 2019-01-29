from django.urls import path

from ingresso.views import erro_Permissao1
from .views import Lista_Evento, Cria_Evento, Listar_Eventos_Por_Promotor, Detalhar_Evento, Atualizar_Evento
from .views import listar_Eventos_Por_Promotor_funcao
urlpatterns = [

    path('new/', Cria_Evento.as_view(), name="create_evento"),
    path('listEventoPromotor/<int:pk>/', Listar_Eventos_Por_Promotor.as_view(), name="list_evento_promotor"),
    path('listEventoPromotor-funcao/<int:id_promotor>/', listar_Eventos_Por_Promotor_funcao, name="list_evento_promotor_funcao"),
    path('informacao-evento/<int:pk>/', Detalhar_Evento.as_view(), name="detalhar_evento"),
    path('atualizar-evento/<int:pk>/', Atualizar_Evento.as_view(), name="editar_evento"),
    path('list/', Lista_Evento.as_view(), name="list_evento"),
    path('sempermissao/', erro_Permissao1, name="erro_permissao1"),
]
