from rest_framework.serializers import ModelSerializer
from .models import Product

# Luego de importar ambas clases podemos crear nuestra clase serializers

class ProductSerializer(ModelSerializer):
    class Meta:
        # Definir el modelo que usara este serializer
        model = Product
        # Definir cuales son los campos que quiero usar los modelos
        # '__all__' = es igual a decir que vamos a usar todos los campos del Modelo(Tablas de la BD)
        fields = '__all__'
