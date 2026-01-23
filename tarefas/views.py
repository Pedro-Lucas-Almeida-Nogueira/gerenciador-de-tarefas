from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer

class UsuarioApiView(APIView):
    
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
