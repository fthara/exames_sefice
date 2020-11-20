from django.shortcuts import render
from django.views.generic import View
from .forms import PacienteForm
from .models import Paciente
from django.http import HttpResponse
from django.template.loader import render_to_string
#from django_tables2 import SingleTableView
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from .tables import PacienteTable
from django.urls import reverse_lazy
from .filters import PacienteFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Cria novos pacientes
def paciente_create_view(request):
    form = PacienteForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form = PacienteForm()
        
        
    context = {
        'form': form
    }
    return render(request, "pacientes/paciente_create.html", context)

# Visualiza os pacientes com o filtro
def PacienteListView(request):
    context = {}
    template_name = 'pacientes/paciente_view2.html'

    filtered_pacientes = PacienteFilter(
        request.GET,
        queryset=Paciente.objects.all()
    )

    context['filtered_pacientes'] = filtered_pacientes

    paginated_filtered_pacientes = Paginator(filtered_pacientes.qs, 2)
    page_number = request.GET.get('page')
    paciente_page_obj = paginated_filtered_pacientes.get_page(page_number)

    try:
        items = paginated_filtered_pacientes.page(page_number)
    except PageNotAnInteger:
        items = paginated_filtered_pacientes.page(1)
    except EmptyPage:
        items = paginated_filtered_pacientes.page(paginated_filtered_pacientes.num_pages)

    index = paciente_page_obj.number - 1
    max_index = len(paginated_filtered_pacientes.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginated_filtered_pacientes.page_range[start_index:end_index]

    context['paciente_page_obj'] = paciente_page_obj
    context['page_range'] = page_range
    context['items'] = items

    return render(request, template_name, context)

# Atualiza dados dos pacientes
class PacienteUpdate(UpdateView):
    model = Paciente
    fields = [
            'rh',
            'nome',
            'data_nascimento',
            'sexo',
            'cor',
        ]
    template_name = 'pacientes/paciente_edit.html'
    success_url = reverse_lazy('busca_paciente')

# Deleta pacientes
class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('busca_paciente')

