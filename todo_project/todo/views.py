from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo_item
# Create your views here.

def home(request):
    latest_todo_items = Todo_item.objects.order_by('date_published')
    context = {"latest_todo_items":latest_todo_items}
    return render(request, "todo/home.html", context)


# class TodoItemDetailView(DetailView):
#      model = Todo_item
#      template_name='todo/todo_item_detail.html'

class TodoCreateView(CreateView): # looks for template as <model>_<form>.html
    model = Todo_item
    fields=['todo_text']

    def form_valid(self, form):
            return super().form_valid(form)
    
class TodoUpdateView(UpdateView):
    model = Todo_item
    fields = ["todo_text", "complete"]


class TodoDeleteView(DeleteView):
    model = Todo_item
    success_url = reverse_lazy("todo-home")