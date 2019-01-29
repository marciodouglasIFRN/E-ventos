from django.db import models
from django.urls import reverse

from clientes.models import Aluno
from promotor.models import PromotorEventos

# Create your models here.

class Evento(models.Model):
    promotores = models.ManyToManyField(PromotorEventos, null=True, blank=True)
    nomeDaAtracao = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    hora_evento = models.TimeField(null=False, blank=False)
    categoria = models.CharField(max_length=30, null=True, blank=True)
    foto = models.ImageField(upload_to='eventos_photos', null=True, blank=True)
    cidade = models.CharField(max_length=50, blank=False)
    rua = models.CharField(max_length=30, blank=False)
    bairro = models.CharField(max_length=20, blank=False)
    numero = models.CharField(max_length=5, blank=False)
    estado = models.CharField(max_length=2, blank=False)
    complemento = models.CharField(max_length=50, blank=False)
    quantidaIngresso = models.CharField(max_length=4)


    def __str__(self):
        return "Evento " + self.nomeDaAtracao

    def get_absolute_url(self):
        return reverse('list_evento')