from django.urls import path
from . import views
from .views import produto_id

urlpatterns = [
    path('', views.index_produtos, name='index_produtos'),
    path('celulares/', views.celulares),
    path('<int:id>', produto_id, name='produto_id'),
]