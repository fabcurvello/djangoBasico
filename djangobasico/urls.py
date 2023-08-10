"""
URL configuration for djangobasico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from produtos import views

urlpatterns = [
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
]

handler404 = views.error404
handler500 = views.error500


'''
Outra forma para a aplicação inicio: 
- Não criar o arquivo urls.py na aplicacao inicio
- Aqui neste arquivo, importar diretamente o método, incluindo no topo deste arquivo:
from inicio.views import index_inicio
- O path aqui neste arquivo ficaria assim:
path('', inicio_index),

- Esta forma é menos indicada nas aplicações, pois, por não termos um arquivo urls.py dentro da aplicação, 
não podemos termos vários subcaminhos, como /produtos e /produtos/celulares. 
- Como a página inicial não possui rotas internas (pois estas já são as aplicações, então este exemplo aqui
só é indicado mesmo neste momento (página inicial)
'''


















