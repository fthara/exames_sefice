"""tecp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view
from pacientes.views import paciente_create_view, PacienteUpdate, PacienteDelete, PacienteListView
from exames_tecp.views import tecp_create_form, Pdf_create_Form#tecp_importa_pdf #FormWizardView
from exames_tecp.forms import PdfForm, ExameTecpForm
from medicos.views import medico_create_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #user auth urls
    path('', home_view, name='home'),
    path('adiciona_paciente', paciente_create_view, name='adiciona_paciente'),
    path('busca_paciente', PacienteListView, name='busca_paciente'),
    path('edita_paciente/<int:pk>/', PacienteUpdate.as_view(), name='edita_paciente'),
    path('exclui_paciente/<int:pk>/', PacienteDelete.as_view(), name='exclui_paciente'),
    path('medico', medico_create_view, name='medico'),
    #path('tecp/adiciona_tecp', FormWizardView.as_view([PdfForm, ExameTecpForm]), name='adiciona_tecp'),
    #path('tecp/importa_pdf', tecp_importa_pdf, name='importa_pdf_tecp')
    path('tecp/adiciona_tecp_p1', Pdf_create_Form, name='adiciona_tecp_p1'),
    path('tecp/adiciona_tecp_p2', tecp_create_form, name='adiciona_tecp_p2')
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
