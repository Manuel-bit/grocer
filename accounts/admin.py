from django.contrib import admin
from .models import Supplier

# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('business_name','contact', 'email')
    ordering = ('business_name',)
    search_fields = ('business_name', 'contact', 'email')

    