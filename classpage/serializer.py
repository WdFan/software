from classpage.models import banji,course
from rest_framework import serializers
from classpage.models import banji,course
from login.serializer import loginUserserializer
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
        fields='__all__'





