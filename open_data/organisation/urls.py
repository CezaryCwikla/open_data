from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrganisationListView.as_view(), name='organisation-home'),
    path('new/', views.OrganisationCreateView.as_view(), name='organisation-create'),
    path('<int:pk>/', views.OrganisationDetailView.as_view(), name='organisation-detail'),
    path('<int:pk>/update/', views.OrganisationUpdateView.as_view(), name='organisation-update'),
    path('<int:pk>/delete/', views.OrganisationDeleteView.as_view(), name='organisation-delete'),

]