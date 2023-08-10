from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_inicio, name='index_inicio'),
]