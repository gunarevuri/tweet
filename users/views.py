from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm,ProfileUpdateForm,EventUpdateForm,UserEventForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import get_template
from django.contrib.auth.models import User
#from django.core.mail import email_user
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .tokens import account_activation_token





def register(request):
	if request.method=='POST':
		p_form=ProfileUpdateForm(request.POST or None)
		u_form=UserRegistrationForm(request.POST or None)
		if u_form.is_valid() and p_form.is_valid():
		    user=u_form.save(commit=False)
		    user.is_active = False
		    user.save()
		    user.refresh_from_db()
		    p_form=ProfileUpdateForm(request.POST or None,instance=user.profile)
		    p_form.full_clean()
		    p_form.save()		    
		    current_site=get_current_site(request)
		    mail_subject='activate ur cynosure account'
		    uid=urlsafe_base64_encode(force_bytes(user.pk))
		    token=account_activation_token.make_token(user)

		    context={'user': user,
                'domain': current_site.domain,
                'uid': uid,


                'token':token,}
		    message=get_template('account_activation_email.html').render(context)
		    user.email_user(mail_subject, message)
		    


		 
		    return render(request,'account_activation_sent.html',{'user':user})


	else:

       


		p_form=ProfileUpdateForm()
		u_form=UserRegistrationForm()







	context={'p_form':p_form,'u_form':u_form}

		

	return render(request,'users/register.html',context)









@login_required
def profile(request):
	if request.method=='POST':
	   p_form = ProfileUpdateForm(request.POST or None,instance=request.user.profile)
	   e_form =EventUpdateForm(request.POST or None,instance=request.user.profile)
	   u_form=UserEventForm(request.POST or None,instance=request.user.profile)
	   if p_form.is_valid() and e_form.is_valid() and u_form.is_valid() :
	   	  p_form.save()
	   	  e_form.save()
	   	  u_form.save()
	   	  username=request.user.username
	   	  messages.success(request,f'{username} profile has been updated successfully')
	   	  return redirect('profile')
	else:
	   p_form=ProfileUpdateForm(instance=request.user.profile)
	   e_form=EventUpdateForm(instance=request.user.profile)
	   u_form=UserEventForm(instance=request.user.profile)


	return render(request,'users/profile.html',{'p_form':p_form,'e_form':e_form,'u_form':u_form})




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64).decode())
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_verified = True
        user.save()
        user.profile.save()
        login(request, user)
        messages.success(request,f'please update your details')

        return redirect('profile')
    else:
        return render(request,'account_activation_invalid.html',{})