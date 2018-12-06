from django.shortcuts import render

# Create your views here.
def promoter(request):
	return render(request, 'promoter.html')