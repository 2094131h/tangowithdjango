from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <a href='about'>About</a> ")
def about(request):
    return HttpResponse("This tutorial has been put together by Craig Hamill 2094131h <a href='../rango/'>Index</a>")

