from django.shortcuts import render ,redirect, Http404
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('todo_deadline')
    print(todos)
    dic = {'todo':todos,'range':range(len(todos))}
    return render(request,'todo/index.html',dic)


def todo_add(request):
    return render(request,'todo/todo-add.html')


def todo_add_fun(request):
    domain = request.POST.get('domain', 'default')
    todo = request.POST.get('todo', 'default')
    deadline = request.POST.get('deadline', 'default')
    status = False
    comment = request.POST.get('comment', 'default')
    Todo.objects.create(todo_domain = domain,todo_work = todo,todo_deadline = deadline,todo_status = status,todo_comment = comment)
    return redirect('TodoHome')

def todo_del(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()
    except Todo.DoesNotExist:
        raise Http404("Todo not found")
    return redirect('TodoHome')

def todo_change_status(request,id):
    todo = Todo.objects.get(id = id)
    status = todo.todo_status
    if status == True:
        status = False
    elif status == False:
        status = True
    todo.todo_status = status
    todo.save()
    return redirect('TodoHome')


