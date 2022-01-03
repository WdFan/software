from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets,status
from login.models import loginUser
from login.serializer import loginUserserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from classpage.serializer import banjiserializer,courseserializer,banjiserializer1,banjiserializer2
from login.models import loginUser
from classpage.models import banji,course
import json
from collections import OrderedDict
import random
import sqlite3
import os
from dbconn import getconn
cur = os.path.abspath(os.path.dirname(os.getcwd()))

alphabet = 'ABCDEFGHIJKLMNOPQISTUVWXYZ'
characters = ''.join(random.sample(alphabet, 5))


class createCourseView(APIView):
    '''创建课程'''
    def post(self,request):
        #数据提交成功
        serializer = courseserializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            #获取老师身份信息
            teacher = self.request.data['teacher']
            courses = course.objects.filter(teacher=teacher)
            serial = courseserializer(courses,many=True)
            return Response({'code':'200','data':serial.data})
        else:
            #数据提交失败
            return Response({'code':'400','data':'error'})


class createBanjiView(APIView):
    '''创建班级'''
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
    '''得到所有的班级'''
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
    '''用户提交邀请码，加入到班级中'''
    def post(self,request):
        #用户名称
        username  = self.request.data['username']
        #班级邀请码
        code = self.request.data['code']
        #查找到该对象
        studentobj = loginUser.objects.filter(username=username).first()
        if studentobj is None:
            return Response({'error': '该学生对象不存在'})
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
        student = loginUser.objects.all().filter(username=username).first()
        banjis = banjiserializer1(student.banji, many=True)
        return Response({'code':200,'data':banjis.data})

class getclassListView(APIView):
    '''找到用户所听的课程'''
    def post(self,request):
        #获取到学生的姓名
        username = self.request.data['username']
        #根据学生查找所在在的班级
        student = loginUser.objects.all().filter(username=username).first()
        if student is None:
            return Response({'error':'该学生不存在'})
        #查找该学生的班级
        banjis = banjiserializer1(student.banji,many=True)
        return Response(banjis.data)

#根据班级id得到班级学生信息
class getClassStudentInfoView(APIView):
    '''根据班级id找到所有的学生'''
    def post(self,requets):
        #获取班级id，找到该班级的所有学生
        id = self.request.data['id']
        ban = banji.objects.all().filter(id = id).first()
        if ban is None:
            return Response({'code':400,'msg':'id不正确'})
        serial = banjiserializer2(ban)
        return Response({'code':'200','studentList':serial.data['student']})

#获取db数据库中的信息
class getdbinfo(APIView):
    '''获取数据库中信息,将数据库中的返回'''
    def post(self,request):
        print(cur)
        conn = getconn()
        if conn is None:
            return Response({'code':400,'msg':'数据库连接出错'})
        cursor = conn.cursor()
        sql = 'select * from users'
        values = cursor.execute(sql)
        data = []
        for i in values:
            sid = i[0]
            sname = i[1]
            sign_time = i[2]
            created_time = i[3]
            face_id = i[4]
            dic = {'sid': sid, 'sname': sname, 'sign_time': sign_time, 'created_time': created_time, 'face_id': face_id}
            data.append(dic)
            dic = {}
        return Response({'code':'200','data':data})
#class editLessonView(APIView):
    #'''变成课程，并且返回最新的课程列表'''



