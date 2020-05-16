from django.contrib import admin

from .models import  UserTweet,Department,Professor,Hostel


admin.site.register(UserTweet)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Hostel)