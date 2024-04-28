
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from script import draw
import logging

logger = logging.getLogger('DJCC')

def hello_world(request):
	return HttpResponse("Hello world")

@require_http_methods(["GET"])
def draw_from_request(request):
    data = request.GET.getlist('data[]')

    if not data:
    	return HttpResponseBadRequest("Uncorrect GET request")

    logger.debug(f"Get data: {data}\n")
    formatted_data = []
    for entry in data:
        formatted_data.append(eval(entry))

    response = HttpResponse(content_type="image/png")

    draw(formatted_data, "img.png")

    with open("img.png", "rb") as f:
        data = f.read()

    response.write(data)

    return response
