from django.forms import ModelForm
from .models import PromotorEventos


class PromoterEventoForm(ModelForm):
    class Meta(object):
        model = PromotorEventos
        fields = ['apelido', 'email', 'senha',
                  'data_nascimento', 'sexo', 'cpf',
                  'telefone','logradouro', 'numero',
                  'complemento','bairro','estado','cidade',
                  'foto','token','status']
