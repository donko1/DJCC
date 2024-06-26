
from django.test import RequestFactory, TestCase
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from PIL import Image
import numpy as np
from .views import (draw_from_request, )



class DrawTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_draw_from_request(self):
        request = self.factory.get('/api/draw_from_request/', {
            'data[]': [
                "{'Open': 100, 'High': 120, 'Low': 100, 'Close': 120}",
                "{'Open': 120, 'High': 125, 'Low': 100, 'Close': 110}",
                "{'Open': 120, 'High': 150, 'Low': 120, 'Close': 150}",
                "{'Open': 150, 'High': 200, 'Low': 140, 'Close': 200}",
                "{'Open': 220, 'High': 240, 'Low': 130, 'Close': 130}",
                "{'Open': 140, 'High': 170, 'Low': 120, 'Close': 120}",
                "{'Open': 110, 'High': 110, 'Low': 90, 'Close': 0}",
            ]
        })

        response = draw_from_request(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/png')


class ImageTest(TestCase):
    def test_images_equal(self):
        src1 = 'DJCC/media/testing.png'  
        src2 = settings.EXAMPLE_PNG_SRC

        image1 = Image.open(src1)
        image2 = Image.open(src2)

        self.assertEqual(image1.size, image2.size, "Изображение не соответствует запросу")

        np.testing.assert_array_equal(np.array(image1), np.array(image2), "Изображение не соответствует запросу")


class MyViewTest(TestCase):
    def test_returns_400(self):
        response = self.client.get('/api/draw_from_request/')
        self.assertEqual(response.status_code, 400)

class AppTests(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1 class="title">DJCC</h1>')
