from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError


year=[1,2,3,4]
branches=['CSE','ECE','EEE','MECHANICAL','CIVIL','IT','OTHERS']


class UserRegistrationForm(UserCreationForm):
	  email=forms.EmailField(label='email', required=True)







	  class Meta:
	  	    model=User
	  	    fields=['username','email','password1','password2']
	  def clean_email(self):
	  	  email=self.cleaned_data['email'].lower()
	  	  r=User.objects.filter(email=email)
	  	  if r.count():
	  	  	 raise ValidationError("email is already exists for some user")
	  	  return email

          





class ProfileUpdateForm(forms.ModelForm):
	  class Meta:
	  	model=Profile
	  	fields=['mobile_number']


class EventUpdateForm(forms.ModelForm):

	  year_of_study=forms.ChoiceField(choices=[(x,x) for x in year])
	  branch=forms.ChoiceField(choices=[(x,x) for x in branches])


	  class Meta:
	      model=Profile
	      fields=['firstname','lastname','branch','year_of_study','college_name','college_location']

class UserEventForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['event1',"event2","event3","event4","event5","event6","event7","event8","event9"]
