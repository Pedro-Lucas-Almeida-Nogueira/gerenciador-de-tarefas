from rest_framework import serializers
from .models import Usuario, Tarefa

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ("nome", "email", "criacao_em", "atualizacao_em")
