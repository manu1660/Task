from rest_framework import serializers
from ProductAPI.models import Products

class ProductsSerializer(serializers.Serializer):
    image=serializers.ImageField(),
    name=serializers.CharField(),
    ram=serializers.CharField(),
    storage=serializers.CharField(),
    display=serializers.CharField(),
    operating_system=serializers.CharField(),
    processor=serializers.CharField(),
    connectivity=serializers.CharField(),
    rear_camera=serializers.CharField(),
    front_Camera=serializers.CharField(),
    battery_charging=serializers.CharField(),
    weight=serializers.CharField(),
    price=serializers.CharField(),
    

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"


    def create(self, validated_data):
        return Products.objects.create(**validated_data)
