from django.shortcuts import render
from django.http import HttpResponse


def input(request):
    return render(request, "input.html")

def result(request):
    return HttpResponse("計算結果を表示")