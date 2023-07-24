from django.shortcuts import render

# Create your views here.
def index_clientes(request):
    return render(request, 'clientes/index.html')





