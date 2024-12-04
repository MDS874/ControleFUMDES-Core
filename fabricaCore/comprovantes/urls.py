# comprovantes/urls.py
from django.urls import path
from . import views
from .views import ComentarComprovanteView


urlpatterns = [
    path('enviar_comprovante/', views.enviar_comprovante, name='enviar_comprovante'),
    path('listar_comprovantes/', views.listar_comprovantes, name='listar_comprovantes'),
    path('<int:id>/detalhes/', views.detalhes_comprovante, name='detalhes_comprovante'),
    path('comentar/', ComentarComprovanteView.as_view(), name='comentar_comprovante'),


]
