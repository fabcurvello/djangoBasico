from django.shortcuts import render
from .models import Cliente


# Create your views here.
def index_clientes(request):
    clientes_db = Cliente.objects.all()
    context = {
        'lista_clientes_db': clientes_db,
    }
    return render(request, 'clientes/index.html', context)


def cliente_id(request, id):
    cliente = Cliente.objects.get(id=id)
    context = {
        'item': cliente,
    }
    return render(request, 'clientes/item_cliente.html', context)


