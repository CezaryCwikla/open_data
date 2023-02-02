from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from .models import Category
from .forms import CategoryCreationForm


class CategoryListView(ListView):
    model = Category
    template_name = 'category/home.html'
    context_object_name = 'categories'
    ordering = ['title']


def create_category(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = CategoryCreationForm(request.POST)
        if form.is_valid():  # All validation rules pass
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Kategoria została utworzona.')
        return redirect('organisation-home')  # Redirect after POST
    else:
        form = CategoryCreationForm()

    return render(request, 'organisation/create_organisation.html', {'form': form})
