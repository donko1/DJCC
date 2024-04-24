
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

    return draw(formatted_data)
