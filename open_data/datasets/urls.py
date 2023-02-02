from django.urls import path
from . import views


urlpatterns = [
    path('', views.DatasetsListView.as_view(), name='datasets-home'),
    path('new/', views.create_dataset, name='datasets-create'),

]