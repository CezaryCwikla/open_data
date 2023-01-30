from django.contrib import admin
from .models import Dataset, Resource, Category, Organisation

admin.site.register(Dataset)
admin.site.register(Resource)
admin.site.register(Category)
admin.site.register(Organisation)
