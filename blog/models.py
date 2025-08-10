from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='cats/')  # this saves image to media/cats/
    img_urls = models.CharField(max_length=100, null=True)
    image_3d = models.CharField(max_length=100, null=True)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title
