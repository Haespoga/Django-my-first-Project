from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from myApp.models import Project, Task
from myApp.forms import createNewTask, createNewProject


# Create your views here.
def index(request):
    title = "Welcome to Django Course !!!"
    return render(request, "index.html",{
        'title' : title
    })

def about(request):
    username = "Haespoga"
    return render(request, "about.html", {
        "username": username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "Projects/projects.html",{
        'projects' : projects
    })

def tasks(request):
    #search = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "Tasks/tasks.html", {
        "tasks" : tasks
    })

def createTask(request):
        if request.method == 'GET':
            # show interface
            return render(request, "Tasks/create_task.html", {
                'form' : createNewTask()
            })
        else:
            Task.objects.create(title = request.POST['title'], description = request.POST['description'], project_id = request.POST['project_id'])
            return redirect('../tasks')

def createProject(request):
    if request.method == 'GET':
        return render(request, 'Projects/create_project.html', {
        'form' : createNewProject()
        })
    else:
        print(request.POST)
        Project.objects.create(name = request.POST["name"])
        return redirect('../projects')