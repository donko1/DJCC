from django.test import RequestFactory, TestCase
from .views import draw_from_request

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