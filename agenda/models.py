from django.db import models


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

    def __str__(self):
        return f"Agendamento de {self.cliente.nome} com {self.massoterapeuta.nome} em {self.data_hora}"
