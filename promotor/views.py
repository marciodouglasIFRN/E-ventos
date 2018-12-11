from django.shortcuts import render

import pyqrcode
# Create your views here.
def promoter(request):
	return render(request, 'promoter.html')

def qrcode(request):
	url =pyqrcode.create('cod=0987654321\nnome=Márcio', version=7)
	url.png('statics/imgs/code.png', scale=8)
	# bola
	return render(request,'qrcode.html')