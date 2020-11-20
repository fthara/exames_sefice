from .models import Paciente
import django_filters

class PacienteFilter(django_filters.FilterSet):
    ORDER_CHOICES = (
        ('ascending', 'Ascendente'),
        ('descending', 'Descendente')
    )

    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino')
    )

    COR_CHOICES = (
        ('Branca', 'Branca'),
        ('Parda', 'Parda'),
        ('Negra', 'Negra'),
        ('Amarela', 'Amarela'),
    )

    ordering = django_filters.ChoiceFilter(label='Ordernar', choices=ORDER_CHOICES, method='filter_by_order')
    rh = django_filters.CharFilter(label='RH')
    nome = django_filters.CharFilter(label='Nome', lookup_expr='icontains')
    data_nascimento = django_filters.CharFilter(label='Data de Nascimento')
    sexo = django_filters.ChoiceFilter(label='Sexo', choices=SEXO_CHOICES)
    cor = django_filters.ChoiceFilter(label='Cor', choices=COR_CHOICES)

    class Meta:
        model = Paciente
        fields = [
            'rh',
            'nome',
            'data_nascimento',
            'sexo',
            'cor',
        ]

    def filter_by_order(self, queryset, name, value):
        expression = 'nome' if value == 'ascending' else '-nome'
        return queryset.order_by(expression)
