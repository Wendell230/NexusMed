from django.contrib import admin
from .models import Paciente, Atendimento

admin.site.register(Paciente)
admin.site.register(Atendimento)
