from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from random import randrange, uniform

# Create your models here.
token = randrange(0, 1000000)
class Pessoa(models.Model):
    apelido = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    senha = models.CharField(max_length=12, null=True, blank=True)
    data_nascimento = models.DateField()
    # data_nascimento = models.CharField(max_length=20, null=True, blank=False)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    logradouro = models.CharField(max_length=50, null=True, blank=True)
    numero = models.CharField(max_length=4, null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True,  blank=True)
    foto = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    token = models.CharField(default=token, max_length=14, blank=True, null=True)
    status = models.BooleanField(default=False)
class Aluno(Pessoa):
    instituicao = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return "APELIDO: " + "/n" + self.email

    def save(self, *args, **kwargs):
        super(Aluno, self).save(*args,**kwargs)
        data = {'email': self.email,'token':token}
        plain_text = render_to_string('clientes/email/novo_aluno.txt', data)
        html_email = render_to_string('clientes/email/novo_aluno.html', data)
        if self.status==False:
            send_mail(
                'Novo Cliente Cadastrado',
                #'O seu pre-cadastro %s foi realizado' % self.first_name,
                plain_text,
                'm.k.m.p.2000@gmail.com',
                ['m.k.m.p.2000@gmail.com'],
                html_message=html_email,
                fail_silently=False,
            )

