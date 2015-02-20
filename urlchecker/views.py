from django.shortcuts import render,render_to_response
from django.http      import HttpResponse
from django.template import Context,loader

def index(request):
    # View code here...
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})
    return HttpResponse(t.render(c))
