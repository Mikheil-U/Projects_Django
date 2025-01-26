from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # pre-populated fields.
    prepopulated_fields = {'slug': ('name', )}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # pre-populated fields.
    prepopulated_fields = {'slug': ('title', )}

    