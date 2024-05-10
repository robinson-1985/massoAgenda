from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'data', 'horario']

class HorarioSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self.get_horas_do_dia()

    @staticmethod
    def get_horas_do_dia():
        # Retorna uma lista de tuplas representando as horas do dia, de 08:00 a 21:00
        return [(f"{hour}:00", f"{hour}:00") for hour in range(8, 22)]
