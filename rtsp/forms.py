from django import forms
from django.core.validators import URLValidator
from .models import CameraFeed


class RTSPLinkField(forms.URLField):
	default_validators = [
	    URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp'))
	]

	def __init__(self, **kwargs):
		kwargs['label'] = 'RTSP Link'
		super().__init__(**kwargs)


class CameraFeedForm(forms.ModelForm):
	url = RTSPLinkField()

	class Meta:
		model = CameraFeed
		fields = ['name', 'url', 'active']


# rtsp://192.168.0.208:554/1/hd
