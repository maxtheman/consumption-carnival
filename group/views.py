from django.shortcuts import render

# Create your views here.

def landing_page(request):
    context = {"username":"poop", "password":"poop"}
    return render(request,'landing.html', context)
