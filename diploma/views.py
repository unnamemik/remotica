from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def diploma(request):
    return render(request, 'content.html')
def structure(request):
    return render(request, "structure.html")

def files(request):
    return render(request, "files.html")

def techno(request):
    return render(request, "techno.html")