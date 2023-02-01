from django.shortcuts import render, redirect
from .models import Dataset
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import DatasetCreationForm


# def home(request):
#     context = {
#         'datasets': Dataset.objects.all()
#     }
#     return render(request, 'datasets/home.html', context)


class DatasetsListView(ListView):
    model = Dataset
    template_name = 'datasets/home.html'
    ordering = ['-date_posted']
    paginate_by = 5


def create_dataset(request):

    if request.method == 'POST':  # If the form has been submitted...
        form = DatasetCreationForm(request.POST)
        if form.is_valid():  # All validation rules pass
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Twoje konto zostało stworzone! Możesz teraz korzystać z konta.')
        return redirect('datasets-home')  # Redirect after POST
    else:
        form = DatasetCreationForm()

    return render(request, 'datasets/create_dataset.html', {'form': form})



