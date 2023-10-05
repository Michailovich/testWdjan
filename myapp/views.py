from django.shortcuts import render
from rest_framework import generics
from .models import Lesson, Product
from .serializers import LessonSerializer, ProductSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Lesson.objects
        return queryset

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product
        return queryset