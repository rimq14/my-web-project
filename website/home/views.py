from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('hello world!')

# def menu(request, ):
#     return render(request, )