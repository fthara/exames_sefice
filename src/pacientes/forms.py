from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):
    rh = forms.CharField(max_length=10, label = 'RH')
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome do Paciente'}), label = 'Nome')
    data_nascimento = forms.DateField(label = 'Data de Nascimento')
    sexo = forms.CharField(max_length=10, label = 'Sexo')
    cor = forms.CharField(max_length=10, label = 'Cor')
    class Meta:
        model = Paciente
        fields = [
            'rh',
            'nome',
            'data_nascimento',
            'sexo',
            'cor',
        ]