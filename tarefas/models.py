from django.db import models

class Base(models.Model):
    criacao_em = models.DateTimeField(auto_now_add=True)
    atualizacao_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tarefa(Base):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
