from django.shortcuts import render


def index(request):
    return render(request, "system/index.html")

# Create your views here.
