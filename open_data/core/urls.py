from django.urls import path
from . import views
from datasets.views import DatasetsListView

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home_search, name='search-home')
]