from django.http import StreamingHttpResponse
import cv2
from .models import CameraFeed


def gen(camera):
	while True:
		ret, frame = camera.read()
		ret, jpeg = cv2.imencode('.jpg', frame)
		yield (b'--frame\r\n'
		       b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def rtsp_feed(request, camera_feed_id):
	camera_feed = CameraFeed.objects.get(id=camera_feed_id)
	return StreamingHttpResponse(
	    gen(cv2.VideoCapture(camera_feed.url)),
	    content_type='multipart/x-mixed-replace; boundary=frame')
