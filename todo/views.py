from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
  todos = Todo.objects.order_by("-date_posted")
  context = {'todos': todos}
  return render(request, "todo/index.html",context)

def add(request):
  return render(request, "todo/add.html") 