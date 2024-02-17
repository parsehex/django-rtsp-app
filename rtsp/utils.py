import cv2

def capture_thumbnail(url):
	cap = cv2.VideoCapture(url)
	ret, frame = cap.read()
	if ret:
		cv2.imwrite('image.jpg', frame)
	cap.release()
	return 'image.jpg'
