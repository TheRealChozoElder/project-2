from django.shortcuts import render,redirect
from .models import TodoTask

def todo_list(request):
    items = TodoTask.objects.all()
    context = {'items':items}
    return render(request, 'todo/todo_list.html', context)

def add_todo(request):
    if request.method == 'POST'
        title = request.POST['title']
        new_item = TodoTask(title=title)
        new_item.save()
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')
