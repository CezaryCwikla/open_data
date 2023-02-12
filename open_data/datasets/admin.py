from django.contrib import admin
from .models import Dataset, Category, Organisation

admin.site.register(Dataset)
admin.site.register(Category)
admin.site.register(Organisation)
