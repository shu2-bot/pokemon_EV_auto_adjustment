from django.shortcuts import render
from django.http import HttpResponse
# from .forms import Calculation_input_form
from .models import Input_Form


def input(request):
    params = {
        "forms": Input_Form(),
    }
    if request.method == "POST":
        pokemon_name = Input_Form(request.POST.get("pokemon_name"))
    
        params = {
            "test_forms": request.POST.get("pokemon_name")
        }

        return render(request, "result.html", params)
    return render(request, "input.html", params)
    # ここでpostメソッドを定義して李サルトに返す？
    

def result(request):
    # ここにPOSTメソッドが来た時に、計算して返却する？
    
    if request.method == "POST":
        pokemon_name = Input_Form(request.POST.get("pokemon_name"))
    
    params = {
        "test_forms": pokemon_name
    }

    return render(request, "result.html", params)
    """
    if request.method == "POST":
        return render(request, "result.html")
        """