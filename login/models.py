from django.db import models
from classpage.models import banji
# Create your models here.
class loginUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    stu_name = models.CharField(max_length=30,null=True,blank=True)
    stu_id = models.CharField(max_length=30,null=True,blank=True)
    stu_school = models.CharField(max_length=30,null=True,blank=True)
    banji = models.ForeignKey(banji,blank=True,related_name='banji',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.username

    