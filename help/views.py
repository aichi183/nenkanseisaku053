from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def help(request):
    template = loader.get_template("help/help.html")
    return HttpResponse(template.render({}, request))