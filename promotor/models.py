from django.db import models
from clientes import models

# Create your models here.
class PromotorEventos(models.Pessoa):

    def __str__(self):
        return "APELIDO: " + self.apelido