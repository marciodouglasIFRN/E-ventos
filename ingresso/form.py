from django.forms import ModelForm
from evento.models import Evento
from .models import Ingresso

class IngressoForm(ModelForm):
    # def __init__(self, evento, *args, **kwargs):
    #     super(IngressoForm, self).__init__(*args, **kwargs)
    #     self.fields['evento'].queryset = Evento.objects.filter(pk=evento)
    def __init__(self, evento, *args, **kwargs):
        ev1 = Evento.objects.filter(pk=evento)

        super(IngressoForm, self).__init__(*args, **kwargs)
        self.fields['evento'].queryset = ev1

    class Meta:
        model = Ingresso
        fields = ['evento', 'aluno']

class IngressoNewEvento(ModelForm):
    def __init__(self, *args, **kwargs):
        ev1 = Evento.objects.filter()
        super(IngressoNewEvento, self).__init__(*args, **kwargs)
        self.fields['evento'].queryset = ev1
        

    class Meta(object):
        model = Ingresso
        fields = ['evento', 'aluno', 'caminho']
