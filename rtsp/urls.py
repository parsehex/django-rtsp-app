from django.urls import path
from . import views

urlpatterns = [
	path(
		'camera_feed_form/',
		views.camera_feed_view,
		name='camera_feed_form'
	),
	path(
		'<int:camera_feed_id>/', views.rtsp_feed, name='rtsp_feed'
	),
]
