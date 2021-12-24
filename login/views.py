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
            return Response({'msg': '登录成功', 'code': 200, 'username': username})
        else:
            return Response({'msg': '登录失败', 'code': 400})
#登陆接口
class RegisterView(APIView):
    def post(self,request):
        postBody = request.body
        info = json.loads(postBody)
        username = info['username']
        password = info['password']
        user_type = info['user_type']
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        #user_type = request.POST.get('user_type')
        user = loginUser.objects.filter(userName=username).first()
        if user:
            return Response({'msg': '注册失败', 'code': 400, 'username': username,'password':password,'user_type':user_type})
        else:
            user = loginUser(userName=username,passWord=password,type=user_type)
            user.save()
            return Response({'msg': '注册成功', 'code': 200, 'username': username,'password': password,'user_type':user_type})
