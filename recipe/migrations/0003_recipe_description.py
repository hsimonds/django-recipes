# Generated by Django 4.1.3 on 2023-01-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_cook_time_recipe_ingredients_recipe_prep_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
    ]
