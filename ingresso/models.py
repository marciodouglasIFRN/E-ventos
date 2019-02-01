from django.db import models

# Create your models here.
from clientes.models import Aluno
from evento.models import Evento


class Ingresso(models.Model):
    evento = models.ManyToManyField(Evento, null=False, blank=False)
    aluno = models.ManyToManyField(Aluno, null=True, blank=True)
    caminho = models.CharField(max_length=70, null=True, blank=True)
    
    def __str__(self):
        return "Ingresso Nº " + str(self.pk)
        