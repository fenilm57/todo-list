from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def showList(request):
    return render(request, 'showList.html')
