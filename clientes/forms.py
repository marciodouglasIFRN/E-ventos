from django.forms import ModelForm
from .models import Aluno


class AlunoForm(ModelForm):
    class Meta(object):
        model = Aluno
        fields = ['nome', 'sobrenome', 'email', 'matricula',
                  'data_nascimento', 'sexo', 'cpf',
                  'telefone','rua', 'numero','bairro',
                  'cidade','estado','foto','token',
                  'status']
