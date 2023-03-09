from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from .forms import Calculation_input_form
from .forms import Calculation_Select_Form 
from .models import My_Pokemon_Input_Form
from .models import Opposite_Pokemon_Input_Form
from .models import Pokemon_status
from .pythonz3 import main_django



def input(request):
    if request.method == "GET":
        params = {
            "my_pokemon_form": My_Pokemon_Input_Form(),
            #"opposite_pokemon_form": Opposite_Pokemon_Input_Form(),
            "opposite_pokemon_form": Calculation_input_form(),
            "calculation_select_form": Calculation_Select_Form(),
        }
        return render(request, "input.html", params)
    
    if request.method != "GET":
        response = HttpResponseNotAllowed(["GET"])
        return response
    

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
        print(speed_list, attack_list, defense_list)
        

        # DBから種族値を取得 forでリストの長さ分だけ回す？
        my_pokemon_bs = Pokemon_status.objects.filter(pokemon_name = pokemon_name_list[0]).values("bs_h", "bs_a", "bs_b", "bs_c", "bs_d", "bs_s")
        opposite_pokemon_bs = Pokemon_status.objects.filter(pokemon_name = pokemon_name_list[1]).values("bs_h", "bs_a", "bs_b", "bs_c", "bs_d", "bs_s")

        # 敵ポケモンのリストを渡すようにする
        # 検証結果はans_listに格納
        ans_list = main_django.main(my_pokemon_bs, opposite_pokemon_bs, opposite_pokemon_ev, speed_list, attack_list, defense_list)
        
        # htmlに表示する時、リストの値をpopして取得するため逆向きにしている
        status_name_list = ["すばやさ", "とくぼう", "とくこう", "ぼうぎょ", "こうげき", "HP"]

        params = {
            "my_pokemon_name": pokemon_name_list[0],
            "my_pokemon_ev_list": ans_list,
            "status_name_list": status_name_list,
        }
        return render(request, "result.html", params)
    
    if request.method != "POST":
        response = HttpResponseNotAllowed(["POST"])
        return response
    