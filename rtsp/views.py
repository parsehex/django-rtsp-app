from django.http import StreamingHttpResponse
import cv2
from django.shortcuts import render, redirect
from .models import CameraFeed
from .forms import CameraFeedForm

def camera_feed_view(request):
	if request.method == 'POST':
		form = CameraFeedForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CameraFeedForm()

	return render(request, 'camera_feed_form.html', {'form': form})

def home(request):
	camera_feeds = CameraFeed.objects.filter(active=True)
	return render(
		request, 'home.html', {'camera_feeds': camera_feeds}
	)

def gen(camera):
	while True:
		ret, frame = camera.read()
		ret, jpeg = cv2.imencode('.jpg', frame)
		yield (
			b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() +
			b'\r\n\r\n'
		)

def rtsp_feed(request, camera_feed_id):
	camera_feed = CameraFeed.objects.get(id=camera_feed_id)
	return StreamingHttpResponse(
		gen(cv2.VideoCapture(camera_feed.url)),
		content_type='multipart/x-mixed-replace; boundary=frame'
	)
