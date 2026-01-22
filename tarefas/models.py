from django.db import models

class Base(models.Model):
    criacao_em = models.DateTimeField(auto_now_add=True)
    atualizacao_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
