from django.contrib import admin
from .models import Agendamento, Cliente, Massoterapeuta

admin.site.register(Agendamento)
admin.site.register(Cliente)
admin.site.register(Massoterapeuta)
