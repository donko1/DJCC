from django.urls import path
from .views import draw_from_request

urlpatterns = [
    path("draw_from_request/", draw_from_request, name="draw_from_request")
]
