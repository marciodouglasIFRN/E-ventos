from django.forms import ModelForm
from .models import Evento


class EventoFormUpdate(ModelForm):
    class Meta:
        model = Evento
        fields = ['promotores', 'nomeDaAtracao', 'descricao',
                  'data', 'foto', 'cidade', 'rua', 'bairro', 'numero',
                  'estado', 'complemento', 'quantidaIngresso']

    def __init__(self, *args, **kwargs):
        super(EventoFormUpdate, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs = {'class': 'form-control', 'row': '40'}

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nomeDaAtracao', 'descricao',
                  'data', 'foto', 'cidade', 'rua', 'bairro', 'numero',
                  'estado', 'complemento', 'quantidaIngresso']