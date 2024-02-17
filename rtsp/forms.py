from django import forms
from django.core.validators import URLValidator
from crispy_forms.helper import FormHelper
from .models import CameraFeed

class RTSPLinkField(forms.URLField):
	default_validators = [
		URLValidator(
			schemes=('http', 'https', 'ftp', 'ftps', 'rtsp')
		)
	]

	def __init__(self, **kwargs):
		kwargs['label'] = 'RTSP Link'
		super().__init__(**kwargs)

class CameraFeedForm(forms.ModelForm):
	url = RTSPLinkField()

	class Meta:
		model = CameraFeed
		fields = ['name', 'url', 'active']
		exclude = ['thumbnail']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
