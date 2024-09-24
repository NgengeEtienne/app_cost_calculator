from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feature(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100)
    hours = models.IntegerField()

    def __str__(self):
        return self.name
