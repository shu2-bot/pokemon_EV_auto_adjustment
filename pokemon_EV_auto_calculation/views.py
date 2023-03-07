from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import Calculation_input_form
from .models import My_Pokemon_Input_Form
from .models import Opposite_Pokemon_Input_Form
from .models import Pokemon_status
from .pythonz3 import main_django
#from . import pythonz3.main_django
#import pythonz3


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
        opposite_pokemon_ev = {"ev_h": ev_h_list[0], "ev_a": ev_a_list[0], "ev_b": ev_b_list[0], "ev_c": ev_c_list[0], "ev_d": ev_d_list[0], "ev_s": ev_s_list[0]}

        # 比較項目
        speed_list = request.POST.getlist("speed")
        attack_list = request.POST.getlist("attack")
        defense_list = request.POST.getlist("defense")

        # DBから種族値を取得 forでリストの長さ分だけ回す？
        my_pokemon_bs = Pokemon_status.objects.filter(pokemon_name = pokemon_name_list[0]).values("bs_h", "bs_a", "bs_b", "bs_c", "bs_d", "bs_s")
        opposite_pokemon_bs = Pokemon_status.objects.filter(pokemon_name = pokemon_name_list[1]).values("bs_h", "bs_a", "bs_b", "bs_c", "bs_d", "bs_s")

        print(my_pokemon_bs[0]["bs_h"])
        print(opposite_pokemon_ev)

        ans_list = main_django.main(my_pokemon_bs, opposite_pokemon_bs, opposite_pokemon_ev, speed_list, attack_list, defense_list)

        # ここでZ3で検証
        print("検証結果")
        my_pokemon_ev_h = ans_list[0]
        my_pokemon_ev_a = ans_list[1]
        my_pokemon_ev_b = ans_list[2]
        my_pokemon_ev_c = ans_list[3]
        my_pokemon_ev_d = ans_list[4]
        my_pokemon_ev_s = ans_list[5]

        params = {
            "my_pokemon_name": pokemon_name_list[0],
            "my_pokemon_ev_h": my_pokemon_ev_h,
            "my_pokemon_ev_a": my_pokemon_ev_a,
            "my_pokemon_ev_b": my_pokemon_ev_b,
            "my_pokemon_ev_c": my_pokemon_ev_c,
            "my_pokemon_ev_d": my_pokemon_ev_d,
            "my_pokemon_ev_s": my_pokemon_ev_s,
        }
        return render(request, "result.html", params)