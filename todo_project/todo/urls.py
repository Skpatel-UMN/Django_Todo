from django.urls import path

from . import views
from .views import TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', views.home, name='todo-home'),
    # path("<int:todo_item_id>/", views.todo_item_detail, name="todo_item_detail"),
    # path("<int:pk>/", TodoItemDetailView.as_view(), name="todo_item_detail"),
    path('todo/add/',TodoCreateView.as_view(), name='todo-create'),
    path('<int:pk>/update/',TodoUpdateView.as_view(), name='todo-update'),
    path('<int:pk>/delete/',TodoDeleteView.as_view(), name='todo-delete')
]