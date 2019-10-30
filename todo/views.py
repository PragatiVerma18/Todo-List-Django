from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
  todos = Todo.objects.order_by("-date_posted")
  context = {'todos': todos}
  return render(request, "todo/index.html",context)

def add(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('home')

  else:
    form = TodoForm()

  context = {'form': form}

  return render(request, "todo/add.html", context) 

def delete_todo(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    
    return redirect('home')
