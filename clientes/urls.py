from django.urls import path
from . import views
from .views import cliente_id

urlpatterns = [
    path('', views.index_clientes, name='index_clientes'),
    path('<int:id>', cliente_id, name='cliente_id'),
]



