from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'useracc/index.html')

def movie(request):
    return render(request, 'useracc/movie.html')

def soccer(request):
    return render(request, 'useracc/soccer.html')

def travel(request):
    return render(request, 'useracc/travel.html')