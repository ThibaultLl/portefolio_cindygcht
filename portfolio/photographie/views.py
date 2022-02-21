from django.shortcuts import render


def photographie(request):
    return render(request, 'photographie/photographie.html')