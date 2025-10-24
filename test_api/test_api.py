from django.http import HttpResponse
from api import api_request

def test_api(request):
    req = api_request.api_request(request)

    return HttpResponse(str(request.headers) + " <br><br>data:" + req.dumps())