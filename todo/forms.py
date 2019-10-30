from django.forms import ModelForm  
from .models import Todo

class TodoForm(ModelForm):
  class Meta:
    model = Todo
    fields = ('text', ) 
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': "What to do next?"})