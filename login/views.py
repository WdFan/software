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
        user = loginUser.objects.filter(username=username).first()
        if user and password==user.password:
            user_info = {'username': username}
            return Response({'msg': '登录成功', 'code': 200, 'user_info': user_info})
        else:
            return Response({'msg': '登录失败，账号或密码错误！', 'code': 400})
#登陆接口
class RegisterView(APIView):
    def post(self,request):
        postBody = request.body
        info = json.loads(postBody)
        username = info['username']
        password = info['password']
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        #user_type = request.POST.get('user_type')
        user = loginUser.objects.filter(username=username).first()
        user_info = {'username': username}
        if user:
            return Response({'msg': '注册失败，用户已存在', 'code': 400, 'user_info': user_info})
        else:
            user = loginUser(username=username,password=password)
            user.save()
            return Response({'msg': '注册成功', 'code': 200, 'user_info': user_info})
