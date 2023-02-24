from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Category
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datasets.models import Dataset
from django.views.generic.list import MultipleObjectMixin

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    ordering = ['title']


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['title', 'file']

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDetailView(DetailView, MultipleObjectMixin):
    model = Category
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Dataset.objects.filter(categories=self.object.id)
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['datasets'] = context['object_list']
        context['datasets_len'] = len(Dataset.objects.filter(categories=self.object.id))
        return context


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['title', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-home')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
# def create_category(request):
#     if request.method == 'POST':  # If the form has been submitted...
#         form = CategoryCreationForm(request.POST)
#         if form.is_valid():  # All validation rules pass
#             form.instance.author = request.user
#             form.save()
#             messages.success(request, f'Kategoria została utworzona.')
#         return redirect('category-home')  # Redirect after POST
#     else:
#         form = CategoryCreationForm()
#
#     return render(request, 'category/category_form.html', {'form': form})
