from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request,'home.html', {})
    #return HttpResponse("<h1>Hello World</h1>")
def about_view(request, *args, **kwargs):
    my_context = {
            "my_text" : "This is my new text",
            "my_num" : 123,
            "my_list" : ['one item', 'two item', 234, 456]

    }
    return render(request,'about.html', my_context)
    #return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):
    return render(request,'contact.html', {})
    #return HttpResponse("<h1>Hello World</h1>")
