from django.db import models

# Create your models here.
class loginUser(models.Model):
    userName = models.CharField(max_length=30)
    passWord = models.CharField(max_length=128)
    type = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.userName

    