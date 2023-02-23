from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Organisation
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import OrganisationCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datasets.models import Dataset

# def home(request):
#     context = {
#         'datasets': Dataset.objects.all()
#     }
#     return render(request, 'datasets/category_list.html', context)


class OrganisationListView(ListView):
    model = Organisation
    context_object_name = 'organisations'
    ordering = ['title']

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # context['num'] = Organisation.objects.all().get('phone').sum()/len(Organisation.objects.all())
    #     # print(context['num'])
    #     sum = 0
    #     for i in Organisation.objects.all():
    #         sum += i.phone
    #     avg = sum/len(Organisation.objects.all())
    #     print(avg)
    #     return context
    #     # #todo !!!!!!!!!!!!!


class OrganisationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Organisation
    fields = ['title',
              'phone',
              'description',
              'address',
              'email',
              'categories',
              'users',
              'image']

    def test_func(self):
        return self.request.user.is_superuser


class OrganisationDetailView(DetailView):
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datasets'] = Dataset.objects.filter(organisation=self.object.id)
        context['datasets_len'] = len(Dataset.objects.filter(organisation=self.object.id))
        return context


class OrganisationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Organisation
    fields = ['title',
              'phone',
              'description',
              'address',
              'email',
              'categories',
              'users',
              'image']

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