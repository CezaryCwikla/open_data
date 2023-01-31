from django.shortcuts import render
from .models import Dataset
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'datasets': Dataset.objects.all()
    }
    return render(request, 'datasets/home.html', context)


class PostListView(ListView):
    model = Dataset
    template_name = 'datasets/home.html'
    context_object_name = 'wnioski'
    ordering = ['-date_posted']
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Dataset
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'datasets/about.html', {'title': 'O mieście'})
