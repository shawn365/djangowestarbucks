# Generated by Django 4.0.1 on 2022-01-07 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_allergy_size_nutrition_image_allergy_drink'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='allergy',
            table='allergies',
        ),
        migrations.AlterModelTable(
            name='allergy_drink',
            table='allergies_drinks',
        ),
        migrations.AlterModelTable(
            name='image',
            table='images',
        ),
        migrations.AlterModelTable(
            name='nutrition',
            table='nutritions',
        ),
        migrations.AlterModelTable(
            name='size',
            table='sizes',
        ),
    ]