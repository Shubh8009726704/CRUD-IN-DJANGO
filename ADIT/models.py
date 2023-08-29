from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    pro_name = models.CharField(max_length=50)
    pro_price = models.IntegerField()
    pro_desc = models.CharField(max_length=50 ,null=True)
    pro_photo = models.ImageField(upload_to='images')