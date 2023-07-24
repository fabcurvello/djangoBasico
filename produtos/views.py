from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_produtos(request):
    return HttpResponse('Página inicial de produtos')

def celulares(request):
    return HttpResponse('Página inicial de Celulares')