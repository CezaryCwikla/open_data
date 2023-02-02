from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category-home'),
    path('new/', views.create_category, name='category-create'),

]