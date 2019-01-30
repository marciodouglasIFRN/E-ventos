from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from random import randrange, uniform

# Create your models here.
# from pygments.lexer import default

token = randrange(0, 1000000)

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    matricula = models.CharField(max_length=20, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    rua = models.CharField(max_length=50, null=True, blank=True)
    numero = models.CharField(max_length=4, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    foto = models.ImageField(upload_to='alunos_photos', null=True, blank=True)
    token = models.CharField(default=token, max_length=14, blank=True, null=True)
    status = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Aluno(Pessoa):
    instituicao = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return "APELIDO: " + "/n" + self.email

    # def save(self, *args, **kwargs):
    #     super(Aluno, self).save(*args, **kwargs)
    #     data = {'pk': self.pk, 'nome': self.nome, 'email': self.email, 'token': token}
    #     plain_text = render_to_string('clientes/email/novo_aluno.txt', data)
    #     html_email = render_to_string('clientes/email/novo_aluno.html', data)
    #     if not self.status:
    #         send_mail(
    #             'Novo Cliente Cadastrado',
    #             #'O seu pre-cadastro %s foi realizado' % self.first_name,
    #             plain_text,
    #             from_email= "KAKAK",
    #             recipient_list=[self.email],
    #             html_message=html_email,
    #             fail_silently=False,
    #         )

        # if self.status==False:
        #     send_mail(
        #         'Novo Cliente Cadastrado',
        #         #'O seu pre-cadastro %s foi realizado' % self.first_name,
        #         plain_text,
        #         'm.k.m.p.2000@gmail.com',
        #         ['m.k.m.p.2000@gmail.com'],
        #         html_message=html_email,
        #         fail_silently=False,
        #     )
        #
    def get_absolute_url(self):
        return reverse('page-home')

