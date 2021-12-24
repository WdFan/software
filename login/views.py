from django.shortcuts import render
from rest_framework import  viewsets
from login.models import loginUser
from login.serializer import loginUserserializer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.
class loginUserViewSet(viewsets.ModelViewSet):
    queryset = loginUser.objects.all()
    serializer_class = loginUserserializer

class LoginView(APIView):
    def post(self,request):
        postBody = request.body
        info = json.loads(postBody)
        username = info['username']
        password = info['password']
        user = loginUser.objects.filter(userName=username).first()
        if user and password==user.passWord:
            return Response({'msg': '登录成功', 'code': 200, 'user_id': user.id})
        else:
            return Response({'msg': '登录失败', 'code': 400})
