from django import forms
from myApp.models import Project

class createNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200)
    description = forms.CharField(label = "Descripcion de la tarea", widget=forms.Textarea)
    project_id = forms.ChoiceField(choices = Project.objects.values_list('id', 'name'))

class createNewProject(forms.Form):
    name = forms.CharField(label="Nombre del nuevo proyecto", max_length = 200)