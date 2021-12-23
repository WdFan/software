from django.db import models

# Create your models here.
class loginUser(models.Model):
    userName = models.CharField(max_length=30)
    passWord = models.CharField(max_length=128)

    def __str__(self):
        return self.userName

    