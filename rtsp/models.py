from django.core import validators
from django.db import models
from django.forms.fields import URLField as FormURLField


class RTSPURLFormField(FormURLField):
	default_validators = [validators.URLValidator(schemes=['rtsp'])]


class RTSPURLField(models.URLField):
	'''URL field that accepts URLs that start with rtsp:// only.'''
	default_validators = [validators.URLValidator(schemes=['rtsp'])]

	def formfield(self, **kwargs):
		return super(RTSPURLField, self).formfield(**{
		    'form_class': RTSPURLFormField,
		})


class CameraFeed(models.Model):
	name = models.CharField(max_length=200)
	url = RTSPURLField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
