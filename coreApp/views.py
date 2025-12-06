from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def help(request):
    return render(request,"help.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
# Create your views here.
