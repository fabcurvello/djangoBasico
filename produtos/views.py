from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_produtos(request):
    context = {
        'produto': 'Tablet iPad', 'preco': '4550.00',
        'produtos': [
            {'produto': 'Smart TV LG 70 Polegadas', 'preco': '5250.00'},
            {'produto': 'Smart TV Samsung 50 Polegadas', 'preco': '3000.00'},
            {'produto': 'Smart TV Philips 42 Polegadas', 'preco': '2100.00'},
        ]
    }
    return render(request, 'produtos/index.html', context)

def celulares(request):
    return HttpResponse('Página inicial de Celulares')
