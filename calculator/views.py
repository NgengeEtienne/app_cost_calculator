from django.http import JsonResponse
from .models import Category, Feature

def calculate_cost(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        feature_ids = request.POST.getlist('features[]')
        
        # Calculate total hours based on selected features
        total_hours = 0
        for feature_id in feature_ids:
            feature = Feature.objects.get(id=feature_id)
            total_hours += feature.hours

        total_cost = total_hours * 10  # $10/hour
        return JsonResponse({'total_cost': total_cost})


from django.shortcuts import render
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'calculator/index.html', {'categories': categories})
