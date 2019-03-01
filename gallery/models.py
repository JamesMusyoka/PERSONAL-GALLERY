from django.db import models

# Create your models here.
class Location(models.Model):
    first_name = models.CharField(max_length =25)

    def __str__(self):
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length =25)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to ='gallery/')
    image_name = models.CharField(max_length =20)
    image_description = models.TextField(max_length =250)
    image_location = models.ForeignKey(Location)
    image_category = models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']