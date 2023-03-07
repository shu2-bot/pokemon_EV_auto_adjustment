from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import Calculation_input_form
from .models import My_Pokemon_Input_Form
from .models import Opposite_Pokemon_Input_Form
from .models import Pokemon_status


def input(request):
    if request.method == "GET":
        params = {
            "my_pokemon_form": My_Pokemon_Input_Form(),
            "opposite_pokemon_form": Opposite_Pokemon_Input_Form(),
        }
        return render(request, "input.html", params)
    
    """
    if request.method == "POST":
        pokemon_name_list = request.POST.getlist("pokemon_name")
        ev_h_list = request.POST.getlist("ev_h")
        ev_a_list = request.POST.getlist("ev_a")
        ev_b_list = request.POST.getlist("ev_b")
        ev_c_list = request.POST.getlist("ev_c")
        ev_d_list = request.POST.getlist("ev_d")
        ev_s_list = request.POST.getlist("ev_s")

        # ここでZ3で検証
        my_pokemon_ev_h = 0
        my_pokemon_ev_a = 0
        my_pokemon_ev_b = 0
        my_pokemon_ev_c = 0
        my_pokemon_ev_d = 0
        my_pokemon_ev_s = 0

        params = {
            "my_pokemon_name": pokemon_name_list[0],
            "my_pokemon_ev_h": my_pokemon_ev_h,
            "my_pokemon_ev_a": my_pokemon_ev_a,
            "my_pokemon_ev_b": my_pokemon_ev_b,
            "my_pokemon_ev_c": my_pokemon_ev_c,
            "my_pokemon_ev_d": my_pokemon_ev_d,
            "my_pokemon_ev_s": my_pokemon_ev_s
        }
        #return render(request, "result.html", params)
        return result(request, params)
    """
    

def result(request):
    if request.method == "POST":
        # [0]調整したいポケモン [1:]相手のポケモン
        pokemon_name_list = request.POST.getlist("pokemon_name")
        
        # 相手のポケモンの努力値
        ev_h_list = request.POST.getlist("ev_h")
        ev_a_list = request.POST.getlist("ev_a")
        ev_b_list = request.POST.getlist("ev_b")
        ev_c_list = request.POST.getlist("ev_c")
        ev_d_list = request.POST.getlist("ev_d")
        ev_s_list = request.POST.getlist("ev_s")

        my_pokemon_bs = Pokemon_status.objects.get(pokemon_name = pokemon_name_list[0])

        # ここでZ3で検証
        my_pokemon_ev_h = 0
        my_pokemon_ev_a = 0
        my_pokemon_ev_b = 0
        my_pokemon_ev_c = 0
        my_pokemon_ev_d = 0
        my_pokemon_ev_s = 0

        params = {
            #"my_pokemon_name": pokemon_name_list[0],
            "my_pokemon_name": my_pokemon_bs,
            "my_pokemon_ev_h": my_pokemon_ev_h,
            "my_pokemon_ev_a": my_pokemon_ev_a,
            "my_pokemon_ev_b": my_pokemon_ev_b,
            "my_pokemon_ev_c": my_pokemon_ev_c,
            "my_pokemon_ev_d": my_pokemon_ev_d,
            "my_pokemon_ev_s": my_pokemon_ev_s
        }
        return render(request, "result.html", params)