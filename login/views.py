from django.shortcuts import render
from rest_framework import  viewsets
from login.models import loginUser
from login.serializer import loginUserserializer
# Create your views here.
class loginUserViewSet(viewsets.ModelViewSet):
    queryset = loginUser.objects.all()
    serializer_class = loginUserserializer
