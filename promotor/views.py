from django.shortcuts import render

import pyqrcode
# Create your views here.
def promoter(request):
	return render(request, 'promoter.html')

def qrcode(request):
	url = pyqrcode.create('https://github.com/marciodouglasIFRN/E-ventos')
	url.png('statics/imgs/code.png', scale=8)
	return render(request,'qrcode.html')