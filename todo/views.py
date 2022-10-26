from django.shortcuts import render
from django.views.generic import ListView, DetailView

from todo.models import TodoModel

# Create your views here.


class TodoList(ListView):
    template_name: str = "list.html"
    model = TodoModel

class TodoDetail(DetailView):
    template_name: str = 'detail.html'
    model = TodoModel