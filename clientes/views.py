from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno
from django.contrib.auth.models import User

# Create your views here.

def cadastrar_new_aluno(request):
	form = AlunoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('page-home')
	return render(request, 'form_Aluno.html',{'form':form})

def cadastrar_new_aluno_email_token(request):
	form = AlunoForm(request.POST or None,request.FILES or None)
	form.save()
	return render(request,'aluno_email.html')

def tela_email(request):
	form = AlunoForm
	return render(request, 'tela_email.html',{'form':form})

def tela_pre_cadastro(request):
	form = AlunoForm(request.GET or None)
	return render(request,'form_Aluno.html',{'form':form})

# def ativar_conta(request, id, token, email):
def ativar_conta(request, token):
	# aluno = get_object_or_404(Aluno, pk=id, email=email,token=token)
	aluno = get_object_or_404(Aluno, token=token)
	form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
	if form.is_valid():
		form.save()
		user = User.objects.create_user(aluno.apelido, aluno.email, aluno.senha)
		user.save()
		# aluno.user = user
		return redirect('page-home')
	return render(request, 'form_Aluno.html', {'form':form })