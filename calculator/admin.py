from django.contrib import admin
from .models import Category, Feature

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show id and name in the list
    search_fields = ('name',)       # Add search functionality

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'hours')  # Show id, name, category, and hours in the list
    list_filter = ('category',)   # Allow filtering by category
    search_fields = ('name',)      # Add search functionality
