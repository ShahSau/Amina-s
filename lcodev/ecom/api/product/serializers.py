from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    class Meta:
        model = Product
        fields = ('id', 'name','price', 'description', 'stock', 'is_active', 'image', 'is_new', 'on_sale', 'category', 'created_at', 'updated_at')