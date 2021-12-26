from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets,status
from login.models import loginUser
from login.serializer import loginUserserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from classpage.serializer import banjiserializer,courseserializer
from login.models import loginUser
from classpage.models import banji,course
import json
from collections import OrderedDict

class createCourseView(APIView):
    def post(self,request):
        #数据提交成功
        serializer = courseserializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            #数据提交失败
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class createBanjiView(APIView):
    def post(self,request):
        #创建班级
        serializer = banjiserializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            #获取到课程号的id
            id = serializer.validated_data.get('couid')
            cou = course.objects.filter(pk=id).first()
            serializer.instance.course = cou
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#得到所交的班级
class getbanjiListView(APIView):
    def post(self,request):
        #postBody = request.body
        #info = json.loads(postBody)
        #username = info['username']
        username = self.request.data['username']
        #找到该用户所教的所有课程
        courses = course.objects.filter(teacher=username)
        #找到后根据课程找到所有班级
        if course is None:
            return {'message': '该用户未创建课程'}
        dict = OrderedDict()
        i = 0
        for c in courses:
            #找到所有的banji对象
            banjis = c.banji.all()
            #创建序列化器
            for banji in banjis:
                serializer = banjiserializer(banji)
                d2 = serializer.data
                dict[i] = d2
                i =i+1
        return Response(dict)













