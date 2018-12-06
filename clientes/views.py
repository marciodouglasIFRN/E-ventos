from django.shortcuts import render
from .forms import AlunoForm
# Create your views here.

def aluno_new(request):
	form = AlunoForm(request.POST or None,request.FILES or None)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect('listar_pessoas_do_bd')
	return render(request, 'form_Aluno.html',{'form':form})