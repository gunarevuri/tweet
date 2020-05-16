from rest_framework import serializers
from Tweet.models import UserTweet
from aacounts.serializers import TweetAccountSerializer

class TweetSerializer(serializers.ModelSerializer):
	  author=TweetAccountSerializer()
	  class Meta:
	  	model=UserTweet
	  	fields=[
                'author',
                'title',
                'content',
                 


	  	        ]