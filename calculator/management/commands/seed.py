from django.core.management.base import BaseCommand
from calculator.models import Category, Feature

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        e_commerce = Category.objects.create(name='E-commerce')
        social_media = Category.objects.create(name='Social Media')
        cloud_kitchen = Category.objects.create(name='Cloud Kitchen')

        Feature.objects.create(category=e_commerce, name='Product Listing', hours=30)
        Feature.objects.create(category=e_commerce, name='Payment Integration', hours=25)
        Feature.objects.create(category=social_media, name='User Profiles', hours=30)
        Feature.objects.create(category=social_media, name='Chat System', hours=40)
        Feature.objects.create(category=cloud_kitchen, name='Menu Display', hours=25)
        Feature.objects.create(category=cloud_kitchen, name='Online Ordering', hours=40)
