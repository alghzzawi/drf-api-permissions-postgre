from rest_framework import serializers
from .models import Coffee,Post

class CoffeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Coffee
        fields=['id','title','purchaser','price','reviewer']

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'