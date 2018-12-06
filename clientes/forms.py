from django.forms import ModelForm
from .models import Aluno


class AlunoForm(ModelForm):
    class Meta(object):
        model = Aluno
        fields = ['apelido', 'email', 'senha', 'data_nascimento', 'sexo', 'cpf','telefone','logradouro','numero','complemento','bairro','estado','cidade','foto','instituicao']
