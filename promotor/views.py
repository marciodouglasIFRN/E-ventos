from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import PromotorEventos
from .form import PromoterEventoForm


# import pyqrcode
# Create your views here.

class Criar_Promotor(CreateView):
    model = PromotorEventos
    fields = [
        'nome', 'sobrenome', 'email', 'matricula',
        'data_nascimento', 'sexo', 'cpf', 'telefone',
        'rua', 'numero', 'bairro', 'cidade', 'estado',
        'foto', 'token', 'status']


class Listar_Promotor(ListView):
    model = PromotorEventos

    def get_queryset(self):
        return PromotorEventos.objects.all()


def promoter(request):
    return render(request, 'promoter.html')


def add_new_promoter(request):
    form = PromoterEventoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('page-home')
    return render(request, 'form_promotorevento.html', {'form': form})

# def qrcode(request):
# 	url = pyqrcode.create('cod=0987654321\nnome=Márcio', version=7)
# 	url.png('statics/imgs/code.png', scale=8)
# 	# bola
# 	return render(request,'qrcode.html')
