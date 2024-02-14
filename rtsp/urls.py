from django.urls import path
from . import views

urlpatterns = [
    path('rtsp_feed/<int:camera_feed_id>/', views.rtsp_feed, name='rtsp_feed'),
]
