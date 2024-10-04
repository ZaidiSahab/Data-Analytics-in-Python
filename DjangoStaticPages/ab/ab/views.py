from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("Youexcel Institute")


def home(request):
      return render(request,"ab/index.html")

def about(request):
    return render(request, 'ab/about.html')

#def Pythoncourse(request):
 #   return HttpResponse("<b>program A,program A<b>")



