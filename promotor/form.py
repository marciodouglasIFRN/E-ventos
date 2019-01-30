from django.forms import ModelForm
from .models import PromotorEventos


class PromoterEventoForm(ModelForm):
    class Meta(object):
        model = PromotorEventos
        fields = ['nome', 'sobrenome', 'email', 'matricula',
                  'data_nascimento', 'sexo', 'cpf',
                  'telefone', 'rua', 'numero', 'bairro',
                  'cidade', 'estado', 'foto', 'token',
                  'status']


class PromoterEventoFormUpdate(ModelForm):
    class Meta(object):
        model = PromotorEventos
        fields = ['nome', 'sobrenome', 'email', 'matricula',
                  'data_nascimento', 'sexo', 'cpf',
                  'telefone', 'rua', 'numero', 'bairro',
                  'cidade', 'estado', 'foto'
                  ]