from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)


class LinkMan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键是User
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=20, default="")
    img = models.CharField(max_length=15, default="")
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    qq = models.CharField(max_length=15)

