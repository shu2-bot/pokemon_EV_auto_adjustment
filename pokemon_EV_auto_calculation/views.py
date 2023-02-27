from django.shortcuts import render
from django.http import HttpResponse


def input(request):
    return render(request, "input.html")

def result(request):
    return render(request, "result.html")