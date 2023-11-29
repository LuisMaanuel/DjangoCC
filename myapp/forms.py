from django import forms
from .models import Project

class CreateNew(forms.Form):
    name = forms.CharField(max_length=200,label='name')
    pais = forms.CharField(max_length=100)
    nodos = forms.CharField(max_length=100)
    num_cores = forms.CharField(max_length=100)
    ram = forms.CharField(max_length=100)
    almacenamiento = forms.CharField(max_length=100)
    teraFlops = forms.CharField(max_length=100)
    SO = forms.CharField(max_length=100)
    
class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'pais', 'nodos', 'num_cores', 'ram', 'almacenamiento', 'teraFlops', 'SO']
