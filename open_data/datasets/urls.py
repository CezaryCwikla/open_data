from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='datasets-home'),
    path('', views.PostListView.as_view(), name='datasets-home'),
    path('about/', views.about, name='datasets-about'),
]