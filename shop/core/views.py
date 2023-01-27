from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render({}, request))


def about(request):
    template = loader.get_template('core/about.html')
    return HttpResponse(template.render({}, request))