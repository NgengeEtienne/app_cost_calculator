from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate-cost/', views.calculate_cost, name='calculate_cost'),
]

