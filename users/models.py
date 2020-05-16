from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	  user=models.OneToOneField(User,on_delete=models.CASCADE)
	  firstname=models.CharField(max_length=20)
	  lastname=models.CharField(max_length=20)
	  branch=models.CharField(max_length=30)
	  year_of_study=models.CharField(max_length=1)
	  college_name=models.CharField(max_length=40)
	  college_location=models.CharField(max_length=20)
	  mobile_number=models.CharField(max_length=10)
	  email_verified=models.BooleanField(default=False)
	  event1=models.BooleanField(default=False)
	  event2=models.BooleanField(default=False)
	  event3=models.BooleanField(default=False)
	  event4=models.BooleanField(default=False)
	  event5=models.BooleanField(default=False)
	  event6=models.BooleanField(default=False)
	  event7=models.BooleanField(default=False)
	  event8=models.BooleanField(default=False)
	  event9=models.BooleanField(default=False)

	  

	  def __str__(self):
	  	  return f'{self.user.username} profile'