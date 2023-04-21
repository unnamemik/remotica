from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    return render(request, "index.html")



@login_required
def postuser(request):
    command = request.POST.get("command", "Undefined")
    token = request.POST.get("token", 1)
    return HttpResponse(f"<h2>Command: {command}   Token: {token}</h2>")


