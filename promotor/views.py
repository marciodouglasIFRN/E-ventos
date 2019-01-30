import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView

from promotor.form import PromoterEventoFormUpdate
from .models import PromotorEventos
from .form import PromoterEventoForm
from django.contrib.auth.models import Group

class Criar_Promotor(CreateView):
    model = PromotorEventos
    fields = [
        'nome', 'sobrenome', 'email', 'matricula',
        'data_nascimento', 'sexo', 'cpf', 'telefone',
        'rua', 'numero', 'bairro', 'cidade', 'estado',
        'foto', 'token', 'status']

    def form_valid(self, form):
        promo = form.save(commit=False)
        username = promo.email
        # senha = random.randit(0, 9999999999)
        promo.user = User.objects.create_user(username=username, password="ifrn2018")
        gp = Group.objects.get(name='promotor')
        gp.user_set.add(promo.user)
        promo.save()
        return super(Criar_Promotor, self).form_valid(form)

class Listar_Promotor(ListView):
    model = PromotorEventos

    def get_queryset(self):
        return PromotorEventos.objects.all()

class AtualizarDadosPromotor(LoginRequiredMixin,UpdateView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('evento.change_evento'):
            return render(request, "evento/sempermissao.html")

        return super(AtualizarDadosPromotor, self).dispatch(request, *args, **kwargs)

    model = PromotorEventos
    form_class = PromoterEventoFormUpdate
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return PromotorEventos.objects.filter(pk=self.kwargs['pk'])



def promoter(request):
    return render(request, 'promoter.html')


def add_new_promoter(request):
    form = PromoterEventoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('page-home')
    return render(request, 'form_promotorevento.html', {'form': form})
