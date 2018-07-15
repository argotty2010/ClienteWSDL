from django.views.generic import CreateView
from .models import Formulario

class editorform(CreateView):
	template_name='Inicio/Form1.html'
	model= Formulario
	