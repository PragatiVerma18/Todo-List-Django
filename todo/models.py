from django.db import models

class Todo(models.Model):
  text = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return 'Todo #{}'.format(self.id)
 
  class Meta:
    verbose_name_plural = 'Todos'