from django.shortcuts import render
from django.http import HttpResponse
from . import api_response
from test_api import test_api

api_list = {
    "test_api": test_api.test_api
}

# fallback for unkown api
def api_not_found(request):
    res = api_response.api_response()
    res.fail("ERR_API_NOT_FOUND")
    return res.get_response()

def index(request, page_slug):
    if page_slug in api_list:
        return api_list[page_slug](request)
    else:
        return api_not_found(request)