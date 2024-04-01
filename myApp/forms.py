from django import forms
from myApp.models import Project

class createNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200, widget = forms.TextInput(attrs = {'class' : 'input'}))
    description = forms.CharField(label = "Descripcion de la tarea", widget=forms.Textarea(attrs = {'class' : 'input'}))
    project_id = forms.ChoiceField(choices = Project.objects.values_list('id', 'name')) 

    def __init__(self, *args, **kwargs):
        super(createNewTask, self).__init__(*args, **kwargs)
        self.fields['project_id'].choices = Project.objects.values_list('id', 'name')

class createNewProject(forms.Form):
    name = forms.CharField(label="Nombre del nuevo proyecto", max_length = 200, widget = forms.TextInput(attrs={'class' : 'input'})) 