from django.contrib import admin
from .models import Usuario, Tarefa

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "criacao_em", "atualizacao_em")

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao", "criacao_em", "atualizacao_em")
