from django.db import models
from cloudinary.models import CloudinaryField   # 🔥 ADD THIS


class Tile(models.Model):

    CATEGORY_CHOICES = [
        ("kitchen", "Kitchen Tiles"),
        ("washroom", "Washroom Tiles"),
        ("bedroom", "Bedroom Tiles"),
        ("living", "Living Room Tiles"),
        ("outdoor", "Outdoor Tiles"),
        ("commercial", "Commercial Space"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()

    # 🔥 CHANGE HERE
    image = CloudinaryField('image')

    description = models.TextField()


class ContactMessage(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sanitary(models.Model):

    CATEGORY_CHOICES = [
        ("commode", "Commode"),
        ("washbasin", "Wash Basin"),
        ("utensil_basin", "Utensil Basin"),
        ("tap", "Tap / Toti"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()

    # 🔥 CHANGE HERE ALSO
    image = CloudinaryField('image')

    description = models.TextField()

    def __str__(self):
        return self.name