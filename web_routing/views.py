from django.shortcuts import render
from django.http import HttpResponse
from . import web_routing
from django.middleware.csrf import get_token

router = web_routing.web_router(False)

# allow if we should treat it as a template
def check_if_file_text(path):
    a = path.split('.')
    file_ext = a[len(a) - 1]

    # if it is a dir then
    if len(a) == 1:
        return True

    text_ext = [".html", ".js", ".css"]

    return file_ext in text_ext
    

# Create your views here.
def index(request, page_path):
    csrf_tok = get_token(request)
    csrf_token_html = '<input type="hidden" id="csrf_token" name="csrf_token" value="{}" />'.format(csrf_tok)

    context = {
        "csrf_token": csrf_token_html
    }

    file_content = router.routing(page_path)

    if check_if_file_text(page_path):
        for d in context:
            file_content = file_content.replace('{%' + d +  '%}', context[d])
    
    return HttpResponse(file_content)
    