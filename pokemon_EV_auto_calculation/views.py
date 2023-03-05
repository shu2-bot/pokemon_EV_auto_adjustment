from django.shortcuts import render
from django.http import HttpResponse
from .forms import Calculation_input_form


def input(request):
    params = {
        "forms": Calculation_input_form(),
    }
    return render(request, "input.html", params)

def result(request):
    return render(request, "result.html")