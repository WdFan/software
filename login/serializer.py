from rest_framework import serializers
from login.models import loginUser

class loginUserserializer(serializers.ModelSerializer):
    class Meta:
        model = loginUser
        fields = ['username','stu_id','stu_name','stu_school']

