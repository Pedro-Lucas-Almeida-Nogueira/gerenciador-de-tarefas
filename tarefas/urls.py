from django.urls import path
from .views import UsuarioApiView, TarefaApiView

urlpatterns = [
    path("usuarios/", UsuarioApiView.as_view(), name="usuarios"),
    path("tarefas/", TarefaApiView.as_view(), name="tarefas")
]
