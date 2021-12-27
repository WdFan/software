from django.db import models

class course(models.Model):
    #开设本课的用户
    teacher = models.CharField(max_length=30,blank=True)
    #课程名称
    name = models.CharField(max_length=30)
    #课程简称
    simple_name = models.CharField(max_length=16)
    #color = models.CharField(max_length=50,blank=True)
    #banji = models.ForeignKey(banji,null=True,blank=True,on_delete=models.CASCADE,related_name='course')
    def __str__(self):
        return self.name


class banji(models.Model):
    colorChoice = (('color0','style0'),
                   ('color1','style1'),
                   ('color2','style2'),
                   ('color3','style3'),
                   )

    #班级名称
    name = models.CharField(max_length=20)
    #开设年份
    year = models.IntegerField(max_length=4)
    #开设季节
    season = models.CharField(max_length=2)
    #用来记录course的id号
    couid = models.IntegerField(default=-1)
    #课程
    course = models.ForeignKey(course,null=True,blank=True,on_delete=models.CASCADE,related_name='banji')
    #学生
    color =  models.CharField(max_length=50,blank=True,choices=colorChoice)
    #student = models.ForeignKey(loginUser,null=True,blank=True,on_delete=models.CASCADE,related_name='banji')
    num = models.IntegerField(blank=True,default=0)


    def __str__(self):
        return self.name



