from django.urls import path
from . import views

app_name= 'ToDo'

urlpatterns = [
    path("", views.home, name='index'),
    path("add", views.addTask, name='add'),
    path("<int:todo_id>/update", views.update, name='update'),
    path("<int:todo_id>/delete/", views.delete, name="delete"),
    path("deleteAll", views.deleteAll, name='deleteAll'),
    path("<int:todo_id>/updateredirect", views.updateredirect, name='updateredirect')
]