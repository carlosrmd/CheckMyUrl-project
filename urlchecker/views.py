from django.shortcuts import render,render_to_response
from django.http      import HttpResponse
from django.template import Context,loader
from django.core.context_processors import csrf
from django import forms
from urlchecker.forms import UrlForm

import os
from urllib.parse import urlparse


def index(request):
    #Redireccion a main
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})         
    return HttpResponse(t.render(c))

def dev(request):
    t = loader.get_template('dev.html')
    c = Context({'foo': 'bar'})
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('about.html')

    path = os.path.dirname(os.path.abspath(__file__))
    path = path + "/static/resp/"
    
    os.chdir(path)

    i=0
    contenidos = []

    for archivo in os.listdir("."):
        for line in open(archivo):
            string = line.rstrip() 
            print(string)
            contenidos.append(string)

        contenidos.append("-")



    c = Context({'archivo': contenidos })
    return HttpResponse(t.render(c))



def isitworking(url):
    # Returns true on successfull ping
    url = urlparse(url) #Stripping url from http
    resultado = os.system("ping -c 1 " + url.netloc)
    return (resultado == 0)

def checking(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        url = request.GET['your_url']
        if url == "": return render(request, 'index.html')
        return render(request, 'respuesta.html',{'cargo':isitworking(url)})
    else:
        form = UrlForm()

    return render(request, 'index.html', {'form': form})