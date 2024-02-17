from django.contrib import admin
from .models import CameraFeed

class CameraFeedAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'active')
	exclude = ('thumbnail', )

admin.site.register(CameraFeed, CameraFeedAdmin)
