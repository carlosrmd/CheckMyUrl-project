from django.shortcuts import render,render_to_response
from django.http      import HttpResponse
from django.template import Context,loader

def index(request):
    # View code here...
    t = loader.get_template('index.html')
    c = Context({'foo': 'bar'})
    return HttpResponse(t.render(c))

def checking(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})