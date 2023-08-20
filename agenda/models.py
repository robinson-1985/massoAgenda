import datetime

from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Massoterapeuta(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    massoterapeuta = models.ForeignKey(Massoterapeuta, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacoes = models.TextField()
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"Agendamento de {self.cliente.nome} com {self.massoterapeuta.nome} em {self.data_hora}"
