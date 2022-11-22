from django.db import models

# Create your models here.

class Supplier(models.Model):
    business_name = models.CharField('Business Name', max_length=100, unique=True)
    caption = models.CharField('Business Caption', max_length=255)
    contact = models.CharField('Contact',max_length=50)
    email = models.EmailField()
    profile = models.ImageField()

    def __str__(self):
        return self.business_name
