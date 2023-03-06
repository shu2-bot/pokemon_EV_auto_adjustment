from django.shortcuts import render
from django.http import HttpResponse
# from .forms import Calculation_input_form
from .models import Input_Form


def input(request):
    params = {
        "forms": Input_Form(),
    }
    return render(request, "input.html", params)

def result(request):
    return render(request, "result.html")