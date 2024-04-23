from django.urls import path
from .views import hello_world, draw_from_request

urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    path("draw_from_request/", draw_from_request, name="draw_from_request")
]
