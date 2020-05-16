from django.urls import path,include
from .views import ListApiView


urlpatterns = [path('',ListApiView.as_view(),name='list_api_view'),







                 ]