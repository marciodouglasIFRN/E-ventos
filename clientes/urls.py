from django.urls import path
from .views import AlunoNovo, AlunoEdit, AtivarConta
#from .views import cadastrar_new_aluno_email_token
#from .views import tela_email
#from .views import tela_pre_cadastro
#from .views import ativar_conta


urlpatterns = [
    path('novo/', AlunoNovo.as_view(), name="create_aluno"),
    path('update/<int:pk>/', AlunoEdit.as_view(), name="edit_aluno"),
    path('ativar/<int:pk>/', AtivarConta.as_view(), name="ativando_conta_aluno"),
#    path('telaemail/', tela_email, name="tela_email_teste"),
 #   path('email/', cadastrar_new_aluno_email_token, name="cadastrar_email_aluno"),
  #  path('pre/', tela_pre_cadastro, name="tela_pre_cadastro_email"),
   # path('ativar/<int:token>/', ativar_conta, name="tela_ativar_conta"),

]
