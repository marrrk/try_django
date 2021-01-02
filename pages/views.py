from django.shortcuts import render
#from django.views import View
from django.http import HttpResponse


# Create your views here.
#class Home1View(View): #trying to use homepage using a class
 #   @classmethod
 #   def as_view(cls, *args, **kwargs):
 #       return HttpResponse("<h1>Hello World<h/1>")


def home2_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Hello World<h/1>")
    return render(request, 'home_extend.html', {})


def context_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'Hello this is a test',
        'my_number': 123,
        'my_list': [1, 2, 3, 'abc'],

    }
    return render(request, 'context.html', my_context)


# look up *args and **kwargs
