from django.urls import path
from .views import UsuarioApiView, TarefaApiView

urlpatterns = [
    path("usuarios/", UsuarioApiView.as_view(), name="usuarios"),
    path("usuarios/<int:pk>", UsuarioApiView.as_view(), name="usuarios"),
    path("tarefas/", UsuarioApiView.as_view(), name="tarefas"),
    path("tarefas/<int:pk>", TarefaApiView.as_view(), name="tarefas")
]
