from django.shortcuts import render


def graphisme(request):
    return render(request, 'graphisme/graphisme.html')