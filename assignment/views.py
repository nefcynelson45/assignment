from django.shortcuts import render
from django.http import FileResponse


def first(request):
    return render(request, "index.html")


def task(request):
    if request.GET.get('dog'):
        img = open('cat.jpeg', 'rb')
        response = FileResponse(img)
        return response
    else:
        img = open('dog.jpg', 'rb')
        response = FileResponse(img)
        return response
