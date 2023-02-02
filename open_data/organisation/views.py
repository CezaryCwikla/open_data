from django.shortcuts import render, redirect
from .models import Organisation
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import OrganisationCreationForm


# def home(request):
#     context = {
#         'datasets': Dataset.objects.all()
#     }
#     return render(request, 'datasets/home.html', context)


class OrganisationListView(ListView):
    model = Organisation
    template_name = 'datasets/home.html'
    ordering = ['title']

#todo przerobic create_views wszedzie
def create_organisation(request):

    if request.method == 'POST':  # If the form has been submitted...
        form = OrganisationCreationForm(request.POST)
        if form.is_valid():  # All validation rules pass
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Organizacja została stworzona.')
        return redirect('organisation-home')  # Redirect after POST
    else:
        form = OrganisationCreationForm()

    return render(request, 'organisation/create_organisation.html', {'form': form})