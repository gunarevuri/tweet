from .models import UserTweet,Department,Professor,Hostel
from django import forms


class TweetCreateForm(forms.ModelForm):


	class Meta:
		model=UserTweet
		fields=['title','content']


class TweetUpdateForm(forms.ModelForm):

	class Meta:
		model=UserTweet
		fields=['title','content']








class Professor_rating_update(forms.ModelForm):

	class Meta:
		model=Professor
		fields=['p_ratings']

class Hostel_rating_update(forms.ModelForm):

	class Meta:
		model=Hostel
		fields=['ratings']