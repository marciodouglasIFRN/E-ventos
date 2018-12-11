from django.urls import path
from .views import cadastrar_new_aluno
from .views import cadastrar_new_aluno_email_token
from .views import tela_email
from .views import tela_pre_cadastro
from .views import ativar_conta


urlpatterns = [
    path('new/', cadastrar_new_aluno, name="cadastrar_nova_pessoa"),
    path('telaemail/', tela_email, name="tela_email_teste"),
    path('email/', cadastrar_new_aluno_email_token, name="cadastrar_email_aluno"),
    path('pre/', tela_pre_cadastro, name="tela_pre_cadastro_email"),
    path('ativar/<int:token>/', ativar_conta, name="tela_ativar_conta"),

]
