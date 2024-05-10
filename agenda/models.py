from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.cliente} - {self.data} {self.horario}"
    
    @staticmethod
    def horarios_disponiveis_para_data(data):
        horarios_agendados = Agendamento.objects.filter(data=data).values_list('horario', flat=True)
        horarios_disponiveis = [hora for hora in Agendamento.get_horas_do_dia() if hora not in horarios_agendados]
        return [(hora, hora) for hora in horarios_disponiveis]

    @staticmethod
    def get_horas_do_dia():
        # Retorna uma lista de strings representando as horas do dia, de 08:00 a 20:00
        return [f"{hour}:00" for hour in range(8, 21)]
