from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sacco/index.html')

def signIn(request):
    return render(request, 'sacco/signIn.html')

def logIn(request):
    return render(request, 'sacco/logIn.html')

def detail(request):
    return render(request, 'sacco/detail.html')