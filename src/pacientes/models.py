from django.db import models

# Create your models here.
class Paciente(models.Model):
    rh = models.CharField(max_length=10, default='00000000')
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField(verbose_name= 'Data de Nascimento')
    sexo = models.CharField(max_length=10)
    cor = models.CharField(max_length=10)

    def __str__(self):
        return self.nome