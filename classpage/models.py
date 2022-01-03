from django.db import models
from login.models import loginUser
class course(models.Model):
    #开设本课的用户
    teacher = models.CharField(max_length=30,blank=True)
    #课程名称
    name = models.CharField(max_length=30)
    #课程简称
    simple_name = models.CharField(max_length=16,blank=True)
    #color = models.CharField(max_length=50,blank=True)
    #banji = models.ForeignKey(banji,null=True,blank=True,on_delete=models.CASCADE,related_name='course')
    def __str__(self):
        return self.name

class banji(models.Model):

    colorChoice = (
                    ('style0','style0'),
                   ('style1','style1'),
                   ('style2','style2'),
                   ('style3','style3'),
                   )

    #班级名称
    name = models.CharField(max_length=20)
    #开设年份
    year = models.IntegerField()
    #开设季节
    season = models.CharField(max_length=2)
    #用来记录course的id号
    couid = models.IntegerField(default=-1)
    #课程
    course = models.ForeignKey(course,null=True,blank=True,on_delete=models.CASCADE,related_name='banji')
    #学生
    color =  models.CharField(max_length=50,blank=True)
    #student = models.ForeignKey(loginUser,null=True,blank=True,on_delete=models.CASCADE,related_name='banji')
    num = models.IntegerField(blank=True,default=0)

    code = models.CharField(max_length=10,blank=True)

    student = models.ManyToManyField(to=loginUser,related_name='banji',blank=True)

    def __str__(self):
        return self.name



'''
import random

alphabet = 'ABCDEFGHIJKLMNOPQISTUVWXYZ'
characters = ''.join(random.sample(alphabet, 5))
print(characters)
'''
