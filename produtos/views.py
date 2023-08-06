from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def index_produtos(request):
    # estes prints foram incluídos para testes do conteúdo do request
    # exibem no terminal o resultado a cada vez que a página de produtos é carregada no browser
    print(dir(request.user)) # exibe tudo o que pode ser feito com request.user
    print(f"DADOS User-Agent: {request.headers['User-Agent']}")
    print(f"DADOS User: {request.user}")

    #Validar se usuário está logado. A var situacao_usuario será passada adiante no context e capturada no HTML Index de Produtos
    if str(request.user) == "AnonymousUser":
        situacao_usuario = "Usuário NÃO Logado"
    else:
        situacao_usuario = "Usuário Logado"

    produtos_db = Produto.objects.all()
    print(f"produtos_db: {produtos_db}")
    context = {
        'lista_produtos_db': produtos_db,
        'produto': 'Tablet iPad', 'preco': '4550.00',
        'logado': situacao_usuario,
        'produtos': [
            {'produto': 'Smart TV LG 70 Polegadas', 'preco': '5250.00'},
            {'produto': 'Smart TV Samsung 50 Polegadas', 'preco': '3000.00'},
            {'produto': 'Smart TV Philips 42 Polegadas', 'preco': '2100.00'},
        ],
    }
    return render(request, 'produtos/index.html', context)


def produto_id(request, id):
    # print(f"--- ID: {id}")
    produto = Produto.objects.get(id=id)
    # print(f"PRODUTO: {produto}")

    context = {
        'item': produto,
    }
    return render(request, 'produtos/item_produto.html', context)


def celulares(request):
    return HttpResponse('Página inicial de Celulares')
