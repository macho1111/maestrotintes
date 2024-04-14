from django.db import models
from django.contrib.auth import get_user_model
from utils.random_string import random_string_generator
User = get_user_model()
# Create your models here.

def slug_maker():
    repeat = True
    while repeat:
        new_slug = random_string_generator()
        counter = Product.objects.filter(slug=new_slug).count()
        if counter == 0:
            repeat = False
    return new_slug

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.name

class Apparel(models.Model):
    apparel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    image = models.ImageField(upload_to='apparel_images', default='default_image.jpg')

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    apparel = models.ForeignKey(Apparel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20, blank=True, default=slug_maker)
    
    def get_shipping_cost(self):
        if self.user.prefecture:
            return self.user.prefecture.shipping_cost
        else:
            return 0
            
    def __str__(self):
        return f"{self.material} - {self.apparel} - {self.apparel.price}"

class ConsentText(models.Model):
    text_id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content