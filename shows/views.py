from django.shortcuts import render, redirect

# Create your views here.
def index(request):\
    return render(request, 'index.html')

def new(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'index.html')

def show(request):
    return render(request, 'index.html')

def allShows(request):
    return render(request, 'index.html')

def editShow(request):
    return render(request, 'index.html')

def updateShow(request):
    return render(request, 'index.html')

def destroyShow(request):
    return render(request, 'index.html')
