from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Organisation
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import OrganisationCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'datasets': Dataset.objects.all()
#     }
#     return render(request, 'datasets/category_list.html', context)


class OrganisationListView(ListView):
    model = Organisation
    context_object_name = 'organisations'
    ordering = ['title']


class OrganisationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Organisation
    fields = ['title',
              'phone',
              'description',
              'address',
              'email',
              'categories',
              'users']

    def test_func(self):
        return self.request.user.is_superuser


class OrganisationDetailView(DetailView):
    model = Organisation


class OrganisationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Organisation
    fields = ['title',
              'phone',
              'description',
              'address',
              'email',
              'categories',
              'users']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class OrganisationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Organisation
    success_url = reverse_lazy('organisation-home')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

# #todo przerobic create_views wszedzie
# def create_organisation(request):
#
#     if request.method == 'POST':  # If the form has been submitted...
#         form = OrganisationCreationForm(request.POST)
#         if form.is_valid():  # All validation rules pass
#             form.instance.author = request.user
#             form.save()
#             messages.success(request, f'Organizacja została stworzona.')
#         return redirect('organisation-home')  # Redirect after POST
#     else:
#         form = OrganisationCreationForm()
#
#     return render(request, 'organisation/organisation_form.html', {'form': form})