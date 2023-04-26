from django.shortcuts import render

# Create your views here.
def structure(request):
    return render(request, "structure.html")

def files(request):
    return render(request, "files.html")

def techno(request):
    return render(request, "techno.html")