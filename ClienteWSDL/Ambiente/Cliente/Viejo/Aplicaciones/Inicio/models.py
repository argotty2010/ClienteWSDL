from django.db import models

# Create your models here.

class Formulario(models.Model):
	TipoPersona=models.CharField(max_length=50)
	consecutivot=models.CharField(max_length=50)
