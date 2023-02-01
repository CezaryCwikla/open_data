from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


class PostListView(ListView):
    model = Category
    template_name = 'datasets/home.html'
    context_object_name = 'categories'
    ordering = ['-date_posted']
