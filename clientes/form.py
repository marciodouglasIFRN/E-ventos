from django.forms import ModelForm
from .models import Aluno


class FormAlunoUpdate(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'matricula',
                  'data_nascimento', 'sexo', 'cpf', 'telefone',
                  'rua', 'numero', 'bairro', 'cidade', 'estado',
                  'foto', 'instituicao']

    def __init__(self, *args, **kwargs):
        super(FormAlunoUpdate, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs = {'required': True}
        self.fields['sobrenome'].widget.attrs = {'required': True}
        self.fields['matricula'].widget.attrs = {'required': True}
        self.fields['data_nascimento'].widget.attrs = {'required': True}
        self.fields['sexo'].widget.attrs = {'required': True}
        self.fields['cpf'].widget.attrs = {'oninput': 'mascara(this,"cpf")', 'required': True}
        self.fields['telefone'].widget.attrs = {'oninput': 'mascara(this,"tel")', 'required': True}
        self.fields['rua'].widget.attrs = {'required': True}
        self.fields['numero'].widget.attrs = {'required': True}
        self.fields['bairro'].widget.attrs = {'required': True}
        self.fields['cidade'].widget.attrs = {'required': True}
        self.fields['estado'].widget.attrs = {'required': True}
        self.fields['instituicao'].widget.attrs = {'required': True}


class FormAluno(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'matricula',
                  'data_nascimento', 'sexo', 'cpf', 'telefone',
                  'rua', 'numero', 'bairro', 'cidade', 'estado',
                  'foto', 'instituicao']