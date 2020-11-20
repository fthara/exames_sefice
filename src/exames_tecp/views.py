from django.shortcuts import render

from django.conf import settings
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import ExameTecpForm, PdfForm

from .models import Exame_TECP, Pdf_TECP

# Create your views here.


"""def tecp_create_form(request):
    #if request.method == 'POST':
    form = ExameTecpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ExameTecpForm()
    else:
        print(form.errors)
        
    context = {
        'form': form
    }
    return render(request, "exames_tecp/exame_create.html", context)

def tecp_importa_pdf(request):
    form = PdfForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ExameTecpForm()
    else:
        print(form.errors)
        
    context = {
        'form': form
    }
    return render(request, "exames_tecp/pdf_form.html", context)"""

"""
class FormWizardView(SessionWizardView):
    template_name = "exames_tecp/exame_create.html"
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))
    form_list = [PdfForm, ExameTecpForm]
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
"""

def Pdf_create_Form(request):
    initial={'pdf': request.session.get('pdf', None)}
    form = PdfForm(request.POST or None, request.FILES or None, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            request.session['pdf'] = form.cleaned_data['pdf']
            return HttpResponseRedirect(reverse('adiciona_tecp_p2'))
    return render(request, 'exames_tecp/pdf_form.html', {'form': form})

def tecp_create_form(request):
    form = ExameTecpForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            tecp = form.save(commit=False)
            pdf = Pdf_TECP.objects.create(pdf=request.session['pdf'])
            tecp.owner = tecp
            tecp.save()
            return HttpResponseRedirect(reverse('exames_tecp/exame_create.html'))
    return render(request, 'exames_tecp/exame_create.html', {'form': form})