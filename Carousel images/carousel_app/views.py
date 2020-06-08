from django.shortcuts import render

# Create your views here.

def carousel_function(request):
    return render (request,'carousel.html',)

