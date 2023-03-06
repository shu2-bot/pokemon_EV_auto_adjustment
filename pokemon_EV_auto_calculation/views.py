from django.shortcuts import render
from django.http import HttpResponse
# from .forms import Calculation_input_form
from .models import My_Pokemon_Input_Form
from .models import Opposite_Pokemon_Input_Form


def input(request):
    if request.method == "GET":
        params = {
            "my_pokemon_form": My_Pokemon_Input_Form(),
            "opposite_pokemon_form": Opposite_Pokemon_Input_Form(),
        }
        return render(request, "input.html", params)
    
    if request.method == "POST":
        pokemon_name = request.POST.get("pokemon_name")
    
        params = {
            "pokemon_name": pokemon_name
        }
        return render(request, "result.html", params)
    

def result(request):
    return 0
    """
    if request.method == "POST":
        pokemon_name = Input_Form(request.POST.get("pokemon_name"))
    
    params = {
        "test_forms": pokemon_name
    }
    return render(request, "result.html", params)
    """

"""
    if request.method == "POST":
        return render(request, "result.html")
        """