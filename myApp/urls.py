from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('hello/<str:username>', views.hello, name = "hello"),
    path('projects/', views.projects, name = "projects"),
    path('projects/<int:id>', views.project_detail, name = "project_detail"),
    path('tasks/', views.tasks, name = "tasks"),
    path('createTask/', views.createTask, name = "createTask"),
    path('createProject/', views.createProject, name = "createProject")
    
]