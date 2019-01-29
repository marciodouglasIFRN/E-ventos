from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import AlunoForm
from django.views.generic import CreateView, ListView, UpdateView

from clientes.form import FormAlunoUpdate
from .models import Aluno
from django.contrib.auth.models import User, Group


class AlunoNovo(CreateView):
    model = Aluno
    fields = [
        'nome', 'sobrenome', 'email', 'matricula',
        'data_nascimento', 'sexo', 'cpf', 'telefone',
        'rua', 'numero', 'bairro', 'cidade', 'estado',
        'foto', 'token', 'status', 'instituicao']

    def form_valid(self, form):
        aluno = form.save(commit=False)
        # username = aluno.nome.split(' ')[0] + aluno.nome.split(' ')[1]
        username = aluno.email
        # aluno.user = User.objects.create_user(username=username, password='ifrn2018')
        aluno.user = User.objects.create_user(username=username, password='ifrn2018')
        gp = Group.objects.get(name='aluno')
        gp.user_set.add(aluno.user)
        aluno.save()
        return super(AlunoNovo, self).form_valid(form)


class AlunoEdit(LoginRequiredMixin, UpdateView):
    model = Aluno
    form_class = FormAlunoUpdate
    # fields = ['nome', 'sobrenome', 'matricula',
    #           'data_nascimento', 'sexo', 'cpf', 'telefone',
    #           'rua', 'numero', 'bairro', 'cidade', 'estado',
    #           'foto', 'instituicao']
    # template_name_field = '_update_form'
    template_name_suffix = '_update_form'


class AtivarConta(UpdateView):
    model = Aluno
    form_class = FormAlunoUpdate
    def get_queryset(self):
        return Aluno.objects.filter(pk=self.kwargs['pk'])

# def cadastrar_new_aluno(request):
# 	form = AlunoForm(request.POST or None, request.FILES or None)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('page-home')
# 	return render(request, 'form_Aluno.html',{'form':form})
#
# def cadastrar_new_aluno_email_token(request):
# 	form = AlunoForm(request.POST or None,request.FILES or None)
# 	form.save()
# 	return render(request,'aluno_email.html')
#
# def tela_email(request):
# 	form = AlunoForm
# 	return render(request, 'tela_email.html',{'form':form})
#
# def tela_pre_cadastro(request):
# 	form = AlunoForm(request.GET or None)
# 	return render(request,'form_Aluno.html',{'form':form})
#
# def ativar_conta(request, id, token, email):
# def ativar_conta(request, token):
	# aluno = get_object_or_404(Aluno, pk=id, email=email,token=token)
	# aluno = get_object_or_404(Aluno, token=token)
	# form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
	# if form.is_valid():
	# 	form.save()
	# 	user = User.objects.create_user(aluno.apelido, aluno.apelido, aluno.senha)
	# 	user = user
	# 	user.save()
	# 	return redirect('page-home')
	# return render(request, 'form_Aluno.html', {'form':form })
