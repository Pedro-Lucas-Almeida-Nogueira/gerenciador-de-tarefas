from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer

class UsuarioApiView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            usuario = Usuario.objects.get(pk=pk)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)

        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    

class TarefaApiView(APIView):

    def get(self, request, pk=None):
        if pk:
            tarefa = Tarefa.objects.get(pk=pk)
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)           

        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
