from django.db import models
from django.utils import timezone


#Bancos=Cargar lista de bancos desde servidor PSE
Bancos=[('Banco uno', 'asdf'), ('Banco dos', 'asdf2')]
class Comment(models.Model):
    name = models.CharField(max_length=20)
    Bancos= models.CharField(label='Seleccione su banco',widget=models.Select(choices=Bancos))

    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)