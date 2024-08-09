from django.contrib import admin
from .models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'category', 'rating', 'phone')

admin.site.register(Company,CompanyAdmin)
