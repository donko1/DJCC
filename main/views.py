from django.http import HttpResponse, HttpResponseBadRequest
from django.conf import settings
import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 

from script import draw

logger = logging.getLogger('DJCC')
HTTP_400_BAD_REQUEST = 400

@api_view(['GET'])
@permission_classes([AllowAny])
def draw_from_request(request):
    data = request.GET.getlist('data[]')

    if not data:
        return Response("Uncorrect GET request", status=HTTP_400_BAD_REQUEST)

    logger.debug(f"Get data: {data}\n")
    formatted_data = []
    for entry in data:
        formatted_data.append(eval(entry))

    data = formatted_data
    draw(data, settings.EXAMPLE_PNG_SRC)

    with open(settings.EXAMPLE_PNG_SRC, "rb") as f:
        data = f.read()

    return HttpResponse(data, content_type="image/png")
