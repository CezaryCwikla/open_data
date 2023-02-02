from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrganisationListView.as_view(), name='organisation-home'),
    path('new/', views.create_organisation, name='organisation-create'),

]