from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class ListView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer