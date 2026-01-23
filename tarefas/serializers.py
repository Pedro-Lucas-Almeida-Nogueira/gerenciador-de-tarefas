from rest_framework import serializers
from .models import Usuario, Tarefa

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ("nome", "email", "criacao_em", "atualizacao_em")

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = ("titulo", "descricao", "criacao_em", "atualizacao_em")
