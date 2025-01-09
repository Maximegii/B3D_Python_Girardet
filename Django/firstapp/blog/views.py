from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def home(request):
    data = {'name':'John Doe'}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))


