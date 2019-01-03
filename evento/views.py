from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .form import EventoFormUpdate
from .models import Evento
from promotor.models import PromotorEventos


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
    fields = ['promotores', 'nomeDaAtracao', 'descricao', 'data', 'foto',
              'cidade', 'rua', 'bairro', 'numero', 'estado', 'complemento',
              'quantidaIngresso']

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


class Listar_Eventos_Por_Promotor(ListView):
    model = Evento
    paginate_by = 2
    def get_queryset(self):
        return Evento.objects.filter(promotores=self.kwargs['pk'])

    template_name_suffix = '_por_promotor'


class Detalhar_Evento(DetailView):
    model = Evento

    def get_queryset(self):
        return Evento.objects.filter(pk=self.kwargs['pk'])


class Atualizar_Evento(UpdateView):
    model = Evento
    form_class = EventoFormUpdate
    # fields = ['promotores', 'nomeDaAtracao', 'descricao',
    #           'data', 'foto', 'cidade', 'rua', 'bairro', 'numero',
    #           'estado', 'complemento', 'quantidaIngresso']
    template_name_suffix = '_update_form'