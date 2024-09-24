from django.urls import path
from . import views
from .views import index, get_features


urlpatterns = [
    path('', views.index, name='index'),
    # path('calculate-cost/', views.calculate_cost, name='calculate_cost'),
    path('get-features/<int:category_id>/', get_features, name='get_features'),

    
]

