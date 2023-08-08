from django.shortcuts import render
from .models import Cliente


# Create your views here.
def index_clientes(request):
    clientes_db = Cliente.objects.all()
    context = {
        'lista_clientes_db': clientes_db,
    }
    return render(request, 'clientes/index.html', context)





