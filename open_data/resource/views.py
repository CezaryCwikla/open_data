from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Resource
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage


# def home(request):
#     context = {
#         'datasets': Dataset.objects.all()
#     }
#     return render(request, 'datasets/category_list.html', context)


class ResourceListView(ListView):
    model = Resource
    context_object_name = 'resources'
    ordering = ['title']


class ResourceDetailView(DetailView):
    model = Resource


class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['title',
              'description',
              'availability',
              'file',
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthing went wrong"})
        return self.render_to_response(context)


class ResourceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resource
    fields = ['title',
              'description',
              'availability',
              'file',
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resource = self.get_object()
        if self.request.user == resource.author or self.request.user.is_superuser:
            return True
        return False


class ResourceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resource
    success_url = reverse_lazy('resource-home')

    def test_func(self):
        wniosek = self.get_object()
        if self.request.user == wniosek.author or self.request.user.is_superuser:
            return True
        return False