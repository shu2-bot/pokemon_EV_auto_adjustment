from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from .forms import Calculation_input_form
from .forms import Calculation_Select_Form 
from .models import My_Pokemon_Input_Form
#from .models import Opposite_Pokemon_Input_Form
from .models import Pokemon_status
from .models import Move_Status
from .models import My_Move_Input_Form
from .models import Opposite_Move_Input_Form
from .pythonz3 import main_django
from urllib.parse import quote
"""
from rest_framework.response import Response
from rest_framework import viewsets
"""


"""
# 同アプリで複数のDBを扱うためのクラス？
class TestViewSet(viewsets.ModelViewSet):
    queryset = ''
    http_method_names = ["get"] # これでGETしかできないようになります

    def list(self, request):
        db1 = DatabaseOne.objects.all() #ここまでは普通のqueryset
        db2 = DatabaseTwo.objects.db_manager("database2").all() # default以外のDB
        return Response({"result": "オッケー！"})
"""


def input(request):
    if request.method == "GET":
        Calculation_Select_Form_List = ["防御力を検証しますか？", "攻撃力を検証しますか？", "素早さを検証しますか？"]
        params = {
            "my_pokemon_form": My_Pokemon_Input_Form(),
            #"opposite_pokemon_form": Opposite_Pokemon_Input_Form(),
            "opposite_pokemon_form": Calculation_input_form(),
            "calculation_select_form": Calculation_Select_Form(),
            "calculation_select_form_list": Calculation_Select_Form_List,
            "my_move_input_form": My_Move_Input_Form(),
            "opposite_move_input_form": Opposite_Move_Input_Form(),
        }
        return render(request, "input.html", params)
    
    if request.method != "GET":
        response = HttpResponseNotAllowed(["GET"])
        return response

def howtouse(request):
    # return HttpResponse(b"Hello, workd!")
    return render(request, "HowToUse.html", {})    

def result(request):
    if request.method == "POST":
        # [0]調整したいポケモン [1:]相手のポケモン
        pokemon_name_list = request.POST.getlist("pokemon_name")
        print("pokemon_name_list = ")
        print(pokemon_name_list)

        # 相手のポケモンの努力値
        ev_h_list = request.POST.getlist("ev_h")
        ev_a_list = request.POST.getlist("ev_a")
        ev_b_list = request.POST.getlist("ev_b")
        ev_c_list = request.POST.getlist("ev_c")
        ev_d_list = request.POST.getlist("ev_d")
        ev_s_list = request.POST.getlist("ev_s")
        opposite_pokemon_ev_list = {"ev_h": ev_h_list, "ev_a": ev_a_list, "ev_b": ev_b_list, "ev_c": ev_c_list, "ev_d": ev_d_list, "ev_s": ev_s_list}

        # 比較項目
        speed_list = request.POST.getlist("speed")
        attack_list = request.POST.getlist("attack")
        defense_list = request.POST.getlist("defense")
        print(speed_list, attack_list, defense_list)

        # ポケモンの技をHTMLから取得
        move_list = request.POST.getlist("move_name")
        print(move_list)

        move_type_category_power_list = []
        for val in move_list:
            if val == "":
                move_type_category_power_list.append("")
            else:
                move_type_category_power = Move_Status.objects.filter(move_name = val).values("type", "category", "power")
                move_type_category_power_list.append(move_type_category_power)
        
        print(move_type_category_power_list)

        # もし検証項目が入力されていなかったら，正しい入力するように促す
        if ("y" not in speed_list) and ("y" not in attack_list) and ("y" not in defense_list):
            return render(request, "none.html")
        
        # 自分のポケモンの種族値を取得
        my_pokemon_bs = Pokemon_status.objects.filter(pokemon_name = pokemon_name_list[0]).values("bs_h", "bs_a", "bs_b", "bs_c", "bs_d", "bs_s", "type1", "type2")
        
        # 相手のポケモンの種族値をリストに追加
        opposite_pokemon_bs_list = []
        for i in range(len(pokemon_name_list) - 1):
            opposite_pokemon_bs = Pokemon_status.objects.filter(pokemon_name = pokemon_name_list[i + 1]).values("bs_h", "bs_a", "bs_b", "bs_c", "bs_d", "bs_s", "type1", "type2")
            opposite_pokemon_bs_list.append(opposite_pokemon_bs)

        # 自分のポケモンの努力値を導くため, それ以外の要素を入力
        # 検証結果はans_listに格納
        ans_list = main_django.main(my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list, speed_list, attack_list, defense_list, move_type_category_power_list)
        
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

"""
def handler404(request, exception):
    context = {
        "request_path": quote(request.path)
    }
    return render(request, "404.html", context, status=404)
"""


def handler403(request, exception):
    return render(request, "403.html", status=403)

def handler400(request, exception):
    return render(request, "400.html", status=400)
