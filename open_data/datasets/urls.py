from django.urls import path
from . import views


urlpatterns = [
    path('', views.DatasetsListView.as_view(), name='datasets-home'),
    path('new/', views.DatasetsCreateView.as_view(), name='datasets-create'),
    path('<int:pk>/', views.DatasetsDetailView.as_view(), name='datasets-detail'),
    path('<int:pk>/update/', views.DatasetsUpdateView.as_view(), name='datasets-update'),
    path('<int:pk>/delete/', views.DatasetsDeleteView.as_view(), name='datasets-delete'),
]