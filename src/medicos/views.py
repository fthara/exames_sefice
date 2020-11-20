from django.shortcuts import render

from .forms import MedicoForm

from .models import Medico

# Create your views here.
def medico_create_view(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MedicoForm()
        
    context = {
        'form': form
    }
    return render(request, "medicos/medico_create.html", context)
