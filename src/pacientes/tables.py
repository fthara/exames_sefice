import django_tables2 as tables
from .models import Paciente

class PacienteTable(tables.Table):
    class Meta:
        model = Paciente
        template_name = "django_tables2/bootstrap4.html"
        fields = [
            'rh',
            'nome',
            'data_nascimento',
            'sexo',
            'cor',
        ]