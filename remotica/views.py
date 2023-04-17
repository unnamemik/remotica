from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
 
def clickSbut(request):
    if request.method == "POST":
        print("Server stated!")
