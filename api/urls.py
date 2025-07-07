from django.urls import path
from . import views

urlpatterns = [
    # مطمئن شوید این مسیر 'videos/' است
    path('videos/', views.video_list, name='video-list'),
]