from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

from todo.models import TodoModel

# Create your views here.


class TodoList(ListView):
    template_name: str = "list.html"
    model = TodoModel

class TodoDetail(DetailView):
    template_name: str = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name: str = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'deadline')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name: str = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')