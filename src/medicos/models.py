from django.db import models

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=120, verbose_name = 'Nome')
    crm = models.CharField(max_length=20, verbose_name = 'CRM')
    cargo = models.CharField(max_length=120,verbose_name = 'Cargo')
