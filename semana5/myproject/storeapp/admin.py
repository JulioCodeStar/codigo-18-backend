from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'is_active')

class ProductAdmin(admin.ModelAdmin):
    # Permite Crear una tupla con los campos que queremos mostrar en el admin
    list_display = ('id', 'nombre', 'price', 'category')
    list_filter = ('category',)

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)