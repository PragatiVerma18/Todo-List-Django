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


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer