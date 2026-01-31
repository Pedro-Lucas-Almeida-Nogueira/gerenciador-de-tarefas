from django.urls import path
from .views import UsuarioApiView, TarefaApiView, UsuariosApiView

urlpatterns = [
    path("usuarios/", UsuariosApiView.as_view(), name="usuarios"),
    path("usuarios/<int:pk>", UsuarioApiView.as_view(), name="usuario"),
    path("tarefas/", TarefaApiView.as_view(), name="tarefas"),
    path("tarefas/<int:pk>", TarefaApiView.as_view(), name="tarefas")
]
