from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets,status
from login.models import loginUser
from login.serializer import loginUserserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from classpage.serializer import banjiserializer,courseserializer,banjiserializer1,banjiserializer2,courseserializer1
from classpage.serializer import messageserializer
from login.models import loginUser
from classpage.models import banji,course,message
import json
from collections import OrderedDict
import random
import sqlite3
import os
from dbconn import getconn
cur = os.path.abspath(os.path.dirname(os.getcwd()))




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
        alphabet = 'ABCDEFGHIJKLMNOPQISTUVWXYZ'
        characters = ''.join(random.sample(alphabet, 5))
        serializer = banjiserializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            #获取到课程号的id
            id = serializer.validated_data.get('couid')
            cou = course.objects.filter(pk=id).first()
            teacher = cou.teacher
            serializer.instance.course = cou
            serializer.instance.code = characters
            serializer.save()
            #查找到teacher，查找该teacher的所有课程
            courses = course.objects.filter(teacher=teacher)
            '''
            ids = []
            for c in courses:
                ids.append(c.id)
            classes = banji.objects.all().filter(couid__in = ids)
            banjiserial = banjiserializer1(classes,many=True)
            return Response({'code':200,'data':banjiserial.data})
            '''
            if course is None:
                return {'code': 400}
            serializer = courseserializer(courses, many=True)
            return Response({'code':200,'data':serializer.data})
        else:
            return Response({'code':400})


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
        couserializer = courseserializer1(banjiobj.course)
        banjiobj.num = len(serializer.data['student'])
        teacher = couserializer.data['teacher']

        if username!= teacher:
            banjiobj.student.add(studentobj)
            banjiobj.num = banjiobj.num+1
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
        id = self.request.data['classId']
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

class editLessonView(APIView):
    '''变成课程，并且返回最新的课程列表,进行更新操作'''
    def put(self,request):
        #获取id，根据id进行操作
        lessonId = self.request.data['lessonId']
        lessForm = self.request.data['lessonForm']
        try:
            lesson = course.objects.all().filter(id = lessonId).first()
        except:
            return Response({'code':400})
        lessonName = lessForm['lessonName']
        lessonSimpleName = lessForm['lessonSimpleName']
        #数据创建
        lesson.name = lessonName
        lesson.simple_name = lessonSimpleName
        lesson.save()
        serializer = courseserializer1(lesson)
        teacher = serializer.data['teacher']
        courses = course.objects.filter(teacher=teacher)
        serial = courseserializer(courses, many=True)
        return Response({'code':'200','data':serial.data})

class savePersonInfoView(APIView):
    def post(self,request):
        personInfoForm = self.request.data['personInfoForm']
        username = personInfoForm['username']
        stu_id = personInfoForm['stu_id']
        stu_name = personInfoForm['stu_name']
        stu_school = personInfoForm['stu_school']
        #筛选出该用户
        user = loginUser.objects.all().filter(username=username).first()
        if user is None:
            return Response({'code':400})
        user.stu_id = stu_id
        user.stu_name = stu_name
        user.stu_school = stu_school
        user.save()
        serializer = loginUserserializer(user)
        return Response({'code':'200','data':serializer.data})


class editClassView(APIView):
     #编辑班级信息
     def put(self,request):
         classId = self.request.data['classId']
         classForm = self.request.data['classForm']
         name = classForm['name']
         year = classForm['year']
         season = classForm['season']
         color = classForm['color']
         lessonId = classForm['lessonId']
         #找到班级进行更新
         ban = banji.objects.all().filter(id=classId).first()
         if ban is None:
             return Response({'code':400})
         ban.name = name
         ban.year = year
         ban.season = season
         ban.color = color
         ban.save()
         #查找教师
         lesson = course.objects.all().filter(id=lessonId).first()
         if lesson is None:
             return Response({'code':400})
         teacher = lesson.teacher
         #查找所有班级
         courses = course.objects.filter(teacher=teacher)
         if course is None:
             return {'message': '该用户未创建课程'}
         serializer = courseserializer(courses, many=True)
         return Response({'code':200,"data":serializer.data})


class getClassInfoView(APIView):
    '''获取班级信息'''
    def post(self,request):
        classId = self.request.data['classId']
        ban = banji.objects.all().filter(id=classId).first()
        if ban is None:
            return Response({'code':400})
        serializer = banjiserializer1(ban)
        return Response({'code':200,'data':serializer.data})
#退出班级
class quitClass(APIView):
    def post(self,request):
        username = self.request.data['username']
        classId = self.request.data['classId']
        ban = banji.objects.all().filter(id=classId).first()
        '''
        serialzier = banjiserializer(ban)
        student  = serialzier.data['student']
        studentobjs = loginUser.objects.all().filter(id__in=student)
        if username not in student:
            return Response({'code':400})
        '''
        student = loginUser.objects.all().filter(username=username).first()
        if ban is None:
            return Response({'code':400})
        if student is None:
            return Response({'code':400})
        ban.student.remove(student)
        ban.num = ban.num-1
        ban.save()
        banjis = banjiserializer1(student.banji, many=True)
        return Response({'code':200,'data':banjis.data})
#删除班级
class deleteClassView(APIView):
    def post(self,request):
        classId = self.request.data['classId']
        ban = banji.objects.all().filter(id=classId).first()
        if ban is None:
            return Response({'code':400})
        serializer =  banjiserializer1(ban)
        teacher = serializer.data['course']['teacher']
        #删除ban
        ban.delete()
        #返回教师的所有班级找到所有班级
        cous = course.objects.all().filter(teacher=teacher)
        serial = courseserializer(cous,many=True)
        return Response({'code': 200, 'data': serial.data})

#删除课程
class deleteLesson(APIView):
    def post(self,request):
        #课程编号
        lessonId = self.request.data['lessonId']
        cou = course.objects.all().filter(id=lessonId).first()
        if cou is None:
            return Response({'code':400})
        couserializer = courseserializer1(cou)
        teacher = couserializer.data['teacher']
        cou.delete()
        cous = course.objects.all().filter(teacher=teacher)
        #返回该课程的所有信息
        serializer = courseserializer(cous,many=True)
        return Response({'code':200,'data':serializer.data})

class getClassMessageView(APIView):
    def post(self,request):
        #获取classId
        classId = self.request.data['classId']
        ban = banji.objects.all().filter(id=classId).first()
        if ban is None:
            return Response({'code':400})
        serializer = messageserializer(ban.message,many=True)
        return Response({'code':200,'data':serializer.data})

#创建消息
class addMessageView(APIView):
    def post(self,request):
        classId = self.request.data['classId']
        messageForm = self.request.data['messageForm']
        createTime = messageForm['createTime']
        title = messageForm['title']
        msg = messageForm['msg']
        ban = banji.objects.all().filter(id=classId).first()
        if ban is None:
            return Response({'code':400})
        Msg = message(createTime=createTime,title=title,msg=msg,banji=ban)
        Msg.save()
        serilaizer = messageserializer(ban.message,many=True)
        return Response({'code':200,'data':serilaizer.data})



