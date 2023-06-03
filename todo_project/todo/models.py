from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Todo_item(models.Model):
    todo_text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date_published = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.todo_text
    
    def get_absolute_url(self):
        return reverse('todo-home')