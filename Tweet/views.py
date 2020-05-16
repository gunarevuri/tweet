from django.shortcuts import render,get_object_or_404,redirect
from .forms import TweetCreateForm,TweetUpdateForm
from .models import UserTweet
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Professor,Department,Hostel
from .forms import Professor_rating_update,Hostel_rating_update



def home(request):
	queryset=UserTweet.objects.all()
	context={'object_list':queryset}
	return render(request,'Tweet/home.html',context)


def contactView(request):
	return render(request,'Tweet/contact.html',{})
@login_required
def createForm(request):
	if request.method=='POST':
		form=TweetCreateForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()


			return redirect('home')
	else:
		form=TweetCreateForm()
	context={'form':form}
	return render(request,'Tweet/createform.html',context)


def detailView(request,id):
	obj=get_object_or_404(UserTweet,id=id)
	context={'object':obj}
	return render(request,'Tweet/detailview.html',context)

@login_required
def deleteView(request,id):
	obj=get_object_or_404(UserTweet,id=id)
	context={'object':obj}
	if request.method=='POST' and request.user==obj.author:
		obj.delete()
		messages.success(request,f'post deleted successfully')
		return redirect('home')
	else:
		if request.user!=obj.author:
			messages.error(request,f'you are not allowed to delete this !!!')
	
		return render(request,'Tweet/deleteform.html',context)


@login_required
def TweetUpdateView(request,id):
	obj=get_object_or_404(UserTweet,id=id)
	context={'object':obj}
	form=TweetUpdateForm(request.POST or None,instance=obj)
	if request.method=='POST' and request.user==obj.author:
				form=TweetUpdateForm(request.POST or None,instance=obj)

				if form.is_valid():
				  form.save()
				  return render(request,'Tweet/detailview.html',context)


	else:
		if request.user!=obj.author:
			messages.error(request,f'you are not allowed to edit this !!!')
	
		form=TweetUpdateForm(instance=obj)
		context={'form':form}
		return render(request,'Tweet/createform.html',context)


@login_required

def department_display(request):
	queryset=Department.objects.all()
	return render(request,'Tweet/department_display.html',{'form':queryset})





@login_required
def professor_display(request,id):
	queryset=Professor.objects.filter(dept_name_id=id)
	return render(request,'Tweet/professor_display.html',{'form':queryset})



def professor_detail_display(request,id):
	obj=get_object_or_404(Professor,id=id)

	return render(request,'Tweet/professor_detail_display.html',{'obj':obj})

@login_required
def hostel_display(request):

	 obj=get_object_or_404(Hostel,id=1)
	 return render(request,'Tweet/hostel_display.html',{'obj':obj})






@login_required
def hostel_update(request,id):
	obj=get_object_or_404(Hostel,id=id)
	context={'obj':obj}
	form=Hostel_rating_update(request.POST or None)
	if request.method=='POST':
		form=Hostel_rating_update(request.POST or None)

		if form.is_valid():
		  a=form.cleaned_data['ratings']
		  


		  if obj.total:
		  	obj.total+=1
		  else:
		  	obj.total=1
		  y=(obj.ratings*(obj.total-1))+a

		  y=y/(obj.total)

		  obj.ratings=y


		  

		  obj.save()

		  return render(request,'Tweet/hostel_display.html',context)
	else:
		
		form=Hostel_rating_update(instance=obj)
		context={'form':form}
		return render(request,'Tweet/hupdate.html',context)


	







def professor_update(request,id):
	obj=get_object_or_404(Professor,id=id)
	context={'obj':obj}
	form=Professor_rating_update(request.POST or None)
	if request.method=='POST':
		form=Professor_rating_update(request.POST or None)

		if form.is_valid():
		  a=form.cleaned_data['p_ratings']  
		  


		  if obj.total:
		  	obj.total+=1
		  else:
		  	obj.total=1
		  y=(obj.p_ratings*(obj.total-1))+a
		  y=y/(obj.total)

		  obj.p_ratings=y


		  

		  obj.save()

		  return render(request,'Tweet/professor_detail_display.html',context)
	else:
		
		form=Professor_rating_update(instance=obj)
		context={'form':form}
		return render(request,'Tweet/pupdate.html',context)


	





