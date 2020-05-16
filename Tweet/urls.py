from django.urls import path
from .views import (home,contactView,createForm,detailView,deleteView,
TweetUpdateView,department_display,professor_display,professor_detail_display,hostel_display,
hostel_update,professor_update)

urlpatterns=[
               path('',home,name='home'),
               path('contact/',contactView,name='contact'),
               path('tweet',createForm,name='tweet'),
               path('tweet/<int:id>/',detailView,name='detail'),
               path('tweet/<int:id>/update/',TweetUpdateView,name='update'),

               path('tweet/<int:id>/delete/',deleteView,name='delete'),
               path('management/hostel/',hostel_display,name='hostel'),
              
               path('management/department/',department_display,name='department'),
               path('professor/<int:id>/',professor_display,name='professor'),
               path('department/professor/<int:id>/',professor_detail_display,name='professor_detail'),
               path('department/professor/<int:id>/update/',professor_update,name='pupdate'),
               path('hostel/',hostel_display,name='hostel'),
               path('hostel/<int:id>/update',hostel_update,name='h_update'),








              




]