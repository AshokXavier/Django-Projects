from django.shortcuts import render

def flights(request):
    return render(request, 'home.html')

def hotels(request):
    return render(request, 'hotels.html')

def trains(request):
    return render(request,'trains.html')