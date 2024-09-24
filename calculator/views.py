from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Feature

def index(request):
    # Get all categories to display in the dropdown
    categories = Category.objects.all()
    return render(request, 'calculator/index.html', {'categories': categories})

def get_features(request, category_id):
    if request.method == 'GET':
        # Retrieve features related to the selected category
        features = Feature.objects.filter(category_id=category_id)
        feature_data = [{'name': feature.name, 'hours': feature.hours} for feature in features]
        return JsonResponse({'features': feature_data})
    return JsonResponse({'error': 'Invalid request'}, status=400)