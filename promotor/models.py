from django.db import models
from clientes import models
from django.urls import reverse

# Create your models here.
class PromotorEventos(models.Pessoa):

    def __str__(self):
        return "Promotor: " + self.email


    def get_absolute_url(self):
        return reverse('page-home')