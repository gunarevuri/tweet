from rest_framework import generics
from .serializers import TweetSerializer
from Tweet.models import UserTweet
from aacounts.serializers import TweetAccountSerializer






class ListApiView(generics.ListAPIView):

	serializer_class=TweetSerializer


	def  get_queryset(self):


		return UserTweet.objects.all()