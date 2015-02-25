from django.shortcuts import render,render_to_response
from django.http      import HttpResponse
from django.template import Context,loader
from django.core.context_processors import csrf
from django import forms
from urlchecker.forms import UrlForm

def index(request):
    # View code here...
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})
    return HttpResponse(t.render(c))

def checking(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        url = request.GET['your_url']
        print(url)
        return render(request, 'index.html')
    else:
        form = UrlForm()

    return render(request, 'index.html', {'form': form})