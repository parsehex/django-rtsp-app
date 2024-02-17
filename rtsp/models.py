from django.core import validators
from django.core.files import File
from django.db import models
from django.forms.fields import URLField as FormURLField
from .utils import capture_thumbnail

class RTSPURLFormField(FormURLField):
	default_validators = [
		validators.URLValidator(schemes=['rtsp'])
	]

class RTSPURLField(models.URLField):
	'''URL field that accepts URLs that start with rtsp:// only.'''
	default_validators = [
		validators.URLValidator(schemes=['rtsp'])
	]

	def formfield(self, **kwargs):
		return super(RTSPURLField, self).formfield(
			**{
				'form_class': RTSPURLFormField,
			}
		)

class CameraFeed(models.Model):
	name = models.CharField(max_length=200)
	url = RTSPURLField()
	active = models.BooleanField(default=True)
	thumbnail = models.ImageField(
		upload_to='thumbnails/', default='default.jpg'
	)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.pk is None or self.url != CameraFeed.objects.get(
			pk=self.pk
		).url:
			# self.thumbnail.delete(save=False)
			p = capture_thumbnail(self.url)
			print(p)
			# self.thumbnail.save(
			# 	'thumbnail.jpg',
			# 	# File(capture_thumbnail(self.url)),
			# 	File(open(p, 'rb')),
			# 	save=True
			# )
			self.thumbnail = File(open(p, 'rb'))
		super().save(*args, **kwargs)
