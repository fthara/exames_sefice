from django.contrib import admin

from .models import Paciente

# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('rh', 'nome', 'sexo')
admin.site.register(Paciente, PacienteAdmin)
