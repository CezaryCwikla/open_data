from django.urls import path
from . import views


urlpatterns = [
    path('', views.ResourceListView.as_view(), name='resource-home'),
    path('new/<int:pk>/', views.ResourceCreateView.as_view(), name='resource-create'),
    path('<int:pk>/', views.ResourceDetailView.as_view(), name='resource-detail'),
    path('<int:pk>/update/', views.ResourceUpdateView.as_view(), name='resource-update'),
    path('<int:pk>/delete/', views.ResourceDeleteView.as_view(), name='resource-delete'),

]