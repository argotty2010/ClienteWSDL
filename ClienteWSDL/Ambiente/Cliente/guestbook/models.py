from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    document = models.CharField(max_length=20)
    documentType = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    emailAddress = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '< {}  {} {}>'.format(self.document, self.firstName ,self.lastName)



# nuevoCliente = Cliente(document=request.POST['document'], documentType=request.POST['documentType'] ,firstName=request.
#POST['firstName'],lastName=request.POST['lastName'],company=request.POST['company'],emailAddress=request.POST['ema
 #ilAddress'],city=request.POST['city'],province=request.POST['province'],country=request.POST['country'],phone=request.POST['phone'],mobile=request.POST['mobile'])
            