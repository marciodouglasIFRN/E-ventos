from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, response
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from evento.form import EventoFormCreate
from promotor.models import PromotorEventos
from .form import EventoFormUpdate
from .models import Evento



# from evento import models
# Create your views here.

# class Evento(models.Evento):


class Cria_Evento(LoginRequiredMixin, CreateView):
    # class Cria_Evento(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # permission_required('evento.add_evento')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('evento.add_evento'):
            # return HttpResponse("Acesso Negado, VOCÊ PRECISA DE PERMISSÃO")
            return render(request, "evento/sempermissao.html")

        return super(Cria_Evento, self).dispatch(request, *args, **kwargs)

    model = Evento
    form_class = EventoFormCreate
    # fields = ['promotores', 'nomeDaAtracao', 'descricao', 'data', 'hora_evento', 'foto',
    #           'cidade', 'rua', 'bairro', 'numero', 'estado', 'complemento',
    #           'quantidaIngresso']

    # def form_valid(self, form):
    #     evento = form.save(commit=False)
    #     # self.request.user.pessoa.pk
    #     evento.promotores.set(self.request.user.pessoa.pk)
    #     evento.save()
    #     return super(Cria_Evento, self).form_valid(form)


class Lista_Evento(ListView):
    models = Evento

    def get_queryset(self):
        return Evento.objects.all()

def listar_Eventos_Por_Promotor_funcao(request, id_promotor):
    evento = get_object_or_404(Evento, promotores=id_promotor)
    promotor = get_object_or_404(PromotorEventos, pk=id_promotor)
    return render(request, 'tempates/listar_eventos_por_promotor_funcao.html',{'formEvento': evento, 'formPromotor':promotor})

class Listar_Eventos_Por_Promotor(ListView):
    model = Evento
    paginate_by = 2

    def get_queryset(self):
        return Evento.objects.filter(promotores=self.kwargs['pk'])

    template_name_suffix = '_por_promotor'


class Listar_Eventos_Por_Categoria(ListView):
    model = Evento

    def get_queryset(self):
        return Evento.objects.filter(categoria=self.kwargs['categoria'])


class Detalhar_Evento(DetailView):
    model = Evento

    def get_queryset(self):
        return Evento.objects.filter(pk=self.kwargs['pk'])


class Atualizar_Evento(LoginRequiredMixin, UpdateView):

    def dispatch(self, request, *args, **kwargs):
        evento = get_object_or_404(Evento, pk=kwargs['pk'])
        if not request.user.has_perm('evento.change_evento'):
            # return HttpResponse("Acesso Negado, VOCÊ PRECISA DE PERMISSÃO")
            return render(request, "evento/sempermissao.html")

        return super(Atualizar_Evento, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        return Evento.objects.filter(Q(pk=self.kwargs['pk']) and Q(promotores=self.request.user.pessoa.promotoreventos.pk))
        # return Evento.objects.filter(pk=self.kwargs['pk'])

    model = Evento
    form_class = EventoFormUpdate
    template_name_suffix = '_update_form'