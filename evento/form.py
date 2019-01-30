from django import forms
from django.forms import ModelForm

from gerenciamentoevento import settings
from .models import Evento


class EventoFormUpdate(ModelForm):
    class Meta:
        model = Evento
        fields = ['promotores', 'nomeDaAtracao', 'descricao','hora_evento','categoria',
                  'data', 'foto', 'cidade', 'rua', 'bairro', 'numero',
                  'estado', 'complemento', 'quantidaIngresso']

    def __init__(self, *args, **kwargs):
        super(EventoFormUpdate, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs = {'class': 'form-control', 'row': '40'}

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nomeDaAtracao', 'descricao','hora_evento', 'categoria',
                  'data', 'foto', 'cidade', 'rua', 'bairro', 'numero',
                  'estado', 'complemento', 'quantidaIngresso']

class EventoFormCreate(ModelForm):
    # data = forms.DateField(
    #     widget=forms.DateInput(format=('%d-%m-%Y'),
    #                            attrs={'class': 'myDateClass',
    #                            'placeholder': 'Select a date'}))
    class Meta:
        model = Evento
        fields = ['promotores', 'nomeDaAtracao', 'descricao', 'data', 'hora_evento', 'foto',
                  'cidade', 'rua', 'bairro', 'numero', 'estado', 'complemento','categoria',
                  'quantidaIngresso']