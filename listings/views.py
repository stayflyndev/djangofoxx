from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


def listings(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
# Create your views here.
