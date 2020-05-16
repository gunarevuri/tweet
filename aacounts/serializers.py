from django.contrib.auth.models import User
from rest_framework import serializers


class TweetAccountSerializer(serializers.ModelSerializer):
	   followers_count=serializers.SerializerMethodField()
	   class Meta:
	   	     model=User
	   	     fields=[
	   	              'username',
	   	              'first_name',
	   	              'last_name',
	   	              'followers_count',]
	   def get_followers_count(self,obj):
	   	     print(obj.username)
	   	     return 0
          
      