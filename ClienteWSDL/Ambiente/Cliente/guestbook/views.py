from django.shortcuts import render, redirect

from .models import Cliente 
from .forms import CommentForm

def index(request):
    comments = Cliente.objects.order_by('-date_added')

    context = {'comments' : comments}

    return render(request, 'guestbook/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            nuevoCliente = Cliente(document=request.POST['document'], documentType=request.POST['documentType'] ,firstName=request.POST['firstName'],lastName=request.POST['lastName'],company=request.POST['company'],emailAddress=request.POST['emailAddress'],city=request.POST['city'],province=request.POST['province'],country=request.POST['country'],phone=request.POST['phone'],mobile=request.POST['mobile'])
            nuevoCliente.save()
            return redirect('index')

    else:
        form = CommentForm()

    context = {'form' : form}
    return render(request, 'guestbook/sign.html', context)