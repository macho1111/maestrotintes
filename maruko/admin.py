from django.contrib import admin
from .models import Material, Apparel, Product, ConsentText
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'apparel', 'material', 'registration_date', 'updated_date']

class ApparelAdmin(admin.ModelAdmin):
    list_display = ['apparel_id', 'name']

admin.site.register(Material) 
admin.site.register(Apparel, ApparelAdmin) 
admin.site.register(Product, ProductAdmin) 
admin.site.register(ConsentText) 
