from django.shortcuts import render

# Create your views here.

def landing_page(request):
    context = {"username":"poop", "password":"poop", "error":"Error!"}
    return render(request,'landing.html', context)
