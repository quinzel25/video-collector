from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add_video'),
    path('video_list', views.video_list, name='video_list'),
    #path routes to page specifically created for that object
    path('video/<int:video_pk>', views.video_details, name='video_details'),
   #this path routes to delete the object associated with selected id
    path('video/<int:video_pk>/delete', views.delete_video, name='delete_video')
]

