from django.contrib import admin
from .models import Cliente, Agendamento
from .forms import AgendamentoForm, HorarioSelect
from django.db import models

class AgendamentoAdmin(admin.ModelAdmin):
    form = AgendamentoForm
    formfield_overrides = {
        models.TimeField: {'widget': HorarioSelect},
    }


admin.site.register(Cliente)
admin.site.register(Agendamento, AgendamentoAdmin)
