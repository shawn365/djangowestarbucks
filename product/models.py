from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    korean_name     = models.CharField(max_length=30)
    english_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'