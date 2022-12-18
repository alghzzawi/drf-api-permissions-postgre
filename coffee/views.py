from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CoffeeSerializers,PostSerializers
from .models import Coffee,Post
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class CoffeeListView(ListCreateAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializers
    permission_classes=[IsAuthenticatedOrReadOnly]

class CoffeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Coffee.objects.all()
    serializer_class= CoffeeSerializers
    permission_classes=[IsOwnerOrReadOnly]

class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializers
    permission_classes=[IsAuthenticatedOrReadOnly]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializers
    permission_classes=[IsAuthenticatedOrReadOnly]