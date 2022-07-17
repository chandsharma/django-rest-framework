from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ["id","price","sale","my_discount", "title","contetnt"]

    def get_my_discount(self,obj):
        print(obj)
        print(obj.id)
        return obj.discount_is()