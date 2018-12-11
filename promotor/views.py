from django.shortcuts import render, redirect, get_object_or_404
from .form import PromoterEventoForm
import pyqrcode
# Create your views here.
def promoter(request):
	return render(request, 'promoter.html')

def add_new_promoter(request):
	form = PromoterEventoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('page-home')
	return render(request, 'form_promotorevento.html', {'form': form})
	
def qrcode(request):
	url =pyqrcode.create('cod=0987654321\nnome=Márcio', version=7)
	url.png('statics/imgs/code.png', scale=8)
	# bola
	return render(request,'qrcode.html')
