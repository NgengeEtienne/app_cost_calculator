from django.urls import path
from django_distill import distill_path
from . import views
from .views import index, get_features

# Distill function to get the homepage (no parameters)
def get_index():
    return None  # No params for homepage

# Distill function for get_features (static export example)
def get_feature_params():
    # If you want to export static pages for specific category IDs, return them here
    for category_id in [1, 2, 3]:  # Example category IDs
        yield {'category_id': category_id}

urlpatterns = [
    path('', views.index, name='index'),
    distill_path('', views.index, name='static_index', distill_func=get_index),  # Static export path for homepage

    path('get-features/<int:category_id>/', get_features, name='get_features'),
    distill_path('get-features/<int:category_id>/', get_features, name='static_get_features', distill_func=get_feature_params),  # Static export path for features
]
