from django.db import models

from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class UserTweet(models.Model):
	  author=models.ForeignKey(User,on_delete=models.CASCADE)
	  title=models.CharField(max_length=10)
	  content=models.TextField()
	  updated=models.DateTimeField(auto_now=True)
	  timestamp=models.DateTimeField(auto_now_add=True)
	  def __str__(self):
	  	  return str(self.title)




class Department(models.Model):
	depart_name=models.CharField(max_length=50)
	dept_code=models.CharField(max_length=10)






class Professor(models.Model):
	dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
	professor_name=models.CharField(max_length=30)
	p_id=models.CharField(max_length=10,unique=True)
	number=models.CharField(max_length=10)
	p_ratings=models.IntegerField(null=True)
	total=models.IntegerField(null=True)



class Hostel(models.Model):
	Hostel_Name=models.CharField(max_length=150,unique=True,null=True)
	ratings=models.IntegerField(null=True)
	total=models.IntegerField(null=True)



	  