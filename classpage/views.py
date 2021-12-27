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
import random

alphabet = 'ABCDEFGHIJKLMNOPQISTUVWXYZ'
characters = ''.join(random.sample(alphabet, 5))


class createCourseView(APIView):
    def post(self,request):
        #数据提交成功
        serializer = courseserializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            #获取老师身份信息
            teacher = self.request.data['teacher']
            courses = course.objects.filter(teacher=teacher)
            serial = courseserializer(courses,many=True)
            return Response(serial.data,status=status.HTTP_200_OK)
        else:
            #数据提交失败
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class createBanjiView(APIView):
    def post(self,request):
        #创建班级
        serializer = banjiserializer(data=self.request.data)
        '''
        if serializer.is_valid():
            serializer.save()
            #找到cou对象
            couid = serializer.validated_data.get('couid')
            cou = course.objects.filter(pk=couid).first()
            #找到
            id = serializer.validated_data.get('id')
            ban = banji.objects.filter(pk=couid).first()
            ban.course = cou
            ban.save()
            return Response({'code':200})
        else:
            return Response({'code':400})
        '''
        if serializer.is_valid():
            serializer.save()
            #获取到课程号的id
            id = serializer.validated_data.get('couid')
            cou = course.objects.filter(pk=id).first()
            serializer.instance.course = cou
            serializer.instance.code = characters
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
        if course is None:
            return {'message': '该用户未创建课程'}
        serializer = courseserializer(courses,many=True)
        return Response(serializer.data)

class joinBanjiView(APIView):
    '''提交邀请码，加入到班级中'''
    def post(self,request):
        #用户名称
        username  = self.request.data['username']
        #班级邀请码
        code = self.request.data['code']
        #查找到该对象
        studentobj = loginUser.objects.filter(username=username).first()
        #根据班级邀请码查找到班级
        banjiobj = banji.objects.filter(code=code).first()
        if banjiobj is None:
            return Response({'error':'该班级对象不存在'})
        serializer = banjiserializer(banjiobj)
        banjiobj.student.add(studentobj)
        #if serializer.is_valid():
        #    serializer.instance.student.add(studentobj)
        #    serializer.save()
        banjiobj.save()
        return Response({'code':200,'msg':'加入班级成功'})







