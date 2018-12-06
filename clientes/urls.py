from django.urls import path
from .views import aluno_new

urlpatterns = [
    path('new/', aluno_new, name="cadastrar_nova_pessoa"),
]
