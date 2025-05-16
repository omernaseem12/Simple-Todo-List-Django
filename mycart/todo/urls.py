from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name= 'TodoHome'),
    path('todo-add',views.todo_add,name= 'todoAdd'),
    path('todo-add-fun',views.todo_add_fun,name= 'todoAddFun'),
    path('todo_del/<int:id>/',views.todo_del,name= 'TodoDel'),
    path('todo_change_status/<int:id>/',views.todo_change_status,name= 'ChangeStatus'),



]