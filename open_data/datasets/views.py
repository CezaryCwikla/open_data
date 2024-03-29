from django.shortcuts import render, redirect
from .models import Dataset
from resource.models import Resource
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import DatasetCreationForm
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, TrigramSimilarity


# def home(request):
#     context = {
#         'datasets': Dataset.objects.all()
#     }
#     return render(request, 'datasets/category_list.html', context)


class DatasetsListView(ListView):
    model = Dataset
    context_object_name = 'datasets'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        keywords = self.request.GET.get('q')
        if keywords:
            # title_vector = SearchVector('title', weight='A')
            # content_vector = SearchVector('description', weight='B')
            # vectors = title_vector + content_vector
            qs = Dataset.objects.annotate(similarity=TrigramSimilarity('title', keywords),
                ).filter(similarity__gt=0.3).order_by('-similarity')
            print(qs)

        else:
            qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs
        else:
            return qs.filter(availability='Publiczne')


class DatasetsCreateView(LoginRequiredMixin, CreateView):
    model = Dataset
    fields = ['title',
              'description',
              'availability',
              'frequency',
              'tags',
              'organisation',
              'categories',
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DatasetsDetailView(DetailView):
    model = Dataset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources'] = Resource.objects.filter(dataset=self.object)
        return context


class DatasetsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dataset
    fields = ['title',
              'description',
              'availability',
              'tags',
              'organisation',
              'categories',
              'resources',
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        dataset = self.get_object()
        if self.request.user == dataset.author or self.request.user.is_superuser:
            return True
        return False


class DatasetsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dataset
    success_url = reverse_lazy('Datasets-home')

    def test_func(self):
        dataset = self.get_object()
        if self.request.user == dataset.author or self.request.user.is_superuser:
            return True
        return False

#
# def create_dataset(request):
#
#     if request.method == 'POST':  # If the form has been submitted...
#         form = DatasetCreationForm(request.POST)
#         if form.is_valid():  # All validation rules pass
#             form.instance.author = request.user
#             form.save()
#             messages.success(request, f'Twoje konto zostało stworzone! Możesz teraz korzystać z konta.')
#         return redirect('datasets-home')  # Redirect after POST
#     else:
#         form = DatasetCreationForm()
#
#     return render(request, 'datasets/dataset_form.html', {'form': form})
