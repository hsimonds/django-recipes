from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    prep_time = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    ingredients = models.TextField()
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='recipe_images')
    date_posted = models.DateTimeField(default=timezone.now)
    # can we update this to preserve recipes that users have saved after original owner deletes?
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-home')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

