from django.test import TestCase
from .models import CameraFeed

class CameraFeedTestCase(TestCase):
    def setUp(self):
        CameraFeed.objects.create(url="rtsp://example.com/feed1")
        CameraFeed.objects.create(url="rtsp://example.com/feed2")

    def test_camera_feeds_have_urls(self):
        """Camera feeds are correctly identified by their URLs"""
        feed1 = CameraFeed.objects.get(url="rtsp://example.com/feed1")
        feed2 = CameraFeed.objects.get(url="rtsp://example.com/feed2")
        self.assertEqual(feed1.url, 'rtsp://example.com/feed1')
        self.assertEqual(feed2.url, 'rtsp://example.com/feed2')