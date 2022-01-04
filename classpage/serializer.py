from classpage.models import banji,course
from rest_framework import serializers
from classpage.models import banji,course,message
from login.serializer import loginUserserializer,loginUserserializer1
#创建序列器
class banjiserializer(serializers.ModelSerializer):
    #student = loginUserserializer(read_only=True)
    #创建班级
    #student_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
    #course = courseserializer(read_only=True)
    #course_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
    #id = serializers.IntegerField()
    #student_id = serializers.ListField()
    class Meta:
        model = banji
        fields = '__all__'

class courseserializer(serializers.ModelSerializer):
    #banji = banjiserializer(read_only=True)
    #用户创建更新外键
    #banji_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
    banji = banjiserializer(many=True,required=False)
    class Meta:
        model = course
        fields= '__all__'


class courseserializer1(serializers.ModelSerializer):
    #banji = banjiserializer(read_only=True)
    #用户创建更新外键
    #banji_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
    #banji = banjiserializer(many=True,required=False)
    class Meta:
        model = course
        fields='__all__'
#班级中包含课程数据
class banjiserializer1(serializers.ModelSerializer):
    #student = loginUserserializer(read_only=True)
    #创建班级
    #student_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
    course = courseserializer1(required=False)
    #course_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)
    #id = serializers.IntegerField()
    #student_id = serializers.ListField()
    class Meta:
        model = banji
        fields = '__all__'

#班级中包含学生数据
class banjiserializer2(serializers.ModelSerializer):
    student = loginUserserializer1(read_only=True,many=True)
    class Meta:
        model = banji
        fields = ['student']

#班级中不包含学生数据
class banjiserializer3(serializers.ModelSerializer):
    course = courseserializer1(required=False)
    class Meta:
        model = banji
        fields = ['id','course','name','year','season','couid','color','num','code']

class messageserializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields =['createTime','title','msg']