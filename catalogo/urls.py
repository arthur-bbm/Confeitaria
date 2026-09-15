from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('bolos/', views.lista_bolos, name='lista_bolos'),
    path('bolos/novo', views.novo_bolo, name='novo_bolo'),
    path('bolos/<int:pk>/', views.bolo_detalhes, name='bolo_detalhes'),
    path('bolos/<int:pk>/editar/', views.editar_bolo, name='editar_bolo'),
    path('bolos/<int:pk>/apagar/', views.apagar_bolo, name='apagar_bolo'),
]