from django import forms

class CommentForm(forms.Form):
    document = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Identificación'}))

    documentType = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Tipo de documento'}))
    firstName = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Nombre'}))
    lastName = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Apellido'}))
    company = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Compañìa'}))
    emailAddress = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Correo Electrónico'}))
    city = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ciudad'}))
    province = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Departamento'}))
    country = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Pais'}))
    phone = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Teléfono'}))
    mobile = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Celular'}))
    #date_added = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Fech'}))
