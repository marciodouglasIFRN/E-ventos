from django.db import models

# Create your models here.

class Pessoa(models.Model):
    apelido = models.CharField(max_length=20,blank=False)
    email = models.CharField(max_length=50,blank=False)
    senha = models.CharField(max_length=12,blank=False)
    data_nascimento = models.DateField(blank=False)
    sexo = models.CharField(max_length=1,blank=False)
    cpf = models.CharField(max_length=15,blank=False)
    telefone = models.CharField(max_length=15,blank=False)
    logradouro = models.CharField(max_length=50,blank=False)
    numero = models.CharField(max_length=4,blank=False)
    complemento = models.CharField(max_length=50,blank=False)
    bairro = models.CharField(max_length=50,blank=False)
    estado = models.CharField(max_length=2,blank=False)
    cidade = models.CharField(max_length=50,blank=False)
    foto = models.ImageField(upload_to='clients_photos', null=True, blank=True)

class Aluno(Pessoa):
    instituicao = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return "APELIDO: " + self.apelido + "/n" + self.email