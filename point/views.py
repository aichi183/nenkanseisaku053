from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def point(request):
    template = loader.get_template("point/point.html")
    return HttpResponse(template.render({}, request))