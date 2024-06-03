from django.shortcuts import render,HttpResponse

# Create your views here.

def home():
    return HttpResponse("hello account")

def register(request):
    pass
    # return render(request,"accounts/login.html")
def login(request):
    return render(request,"accounts/login.html")


def logout(request):
    return render(request,"accounts/logout.html")