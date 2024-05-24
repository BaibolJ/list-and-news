
from django.shortcuts import render
from .models import Object

def index(request):
    objects = Object.objects.all()
    context = {
        'objects': objects
    }
    return render(request, 'app/index.html', context)

def detail(request, pk):
    obj = Object.objects.get( pk=pk )
    context = {
        'object': obj
    }
    return render(request, 'app/detail.html', context)