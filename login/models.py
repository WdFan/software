from django.db import models

# Create your models here.
class loginUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.username

    