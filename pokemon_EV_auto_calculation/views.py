#from django.shortcuts import render
from django.http import HttpResponse


def input(request):
    return HttpResponse("ポケモンの値を入力")

def result(request):
    return HttpResponse("計算結果を表示")