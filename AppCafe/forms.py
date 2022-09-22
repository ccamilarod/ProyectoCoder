from socket import fromshare
from django import forms


class CafeFormulario(forms.Form):

    origen = forms.CharField()
    molienda = forms.CharField()

class MetodoFormulario(forms.Form):

    metodo = forms.CharField()

class PesoFormulario(forms.Form):

    gramos = forms.IntegerField()