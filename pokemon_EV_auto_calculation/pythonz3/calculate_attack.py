from z3 import *
from . import calculate


def calculate_attack(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, min_sev, attack_list, attack_move_list, my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list):
    # ソルバーを複製
    s_copy = Solver()
    # sの制約をコピーに追加
    for c in s.assertions():
        s_copy.add(c)
    s_copy.add(ev_h == 0)
    s_copy.add(ev_b == 0)
    s_copy.add(ev_d == 0)
    s_copy.add(ev_s == min_sev)

    for i in range(len(attack_list)):
        if attack_list[i] == "y":
            print(attack_move_list)
            if attack_move_list[i][0]["category"] == "physical":
                compare_attack()
            # s_copyに条件を追加
            elif attack_move_list[i][0]["category"] == "special":
                compare_spacial_attack(s_copy, ev_c, my_pokemon_bs[0]["bs_c"], opposite_pokemon_ev_list["ev_h"][i], opposite_pokemon_bs_list[i][0]["bs_h"], opposite_pokemon_ev_list["ev_d"][i], opposite_pokemon_bs_list[i][0]["bs_d"], attack_move_list[i][0]["power"], attack_move_list[i][0]["type"], my_pokemon_bs[0]["type1"], my_pokemon_bs[0]["type2"], opposite_pokemon_bs_list[i][0]["type1"], opposite_pokemon_bs_list[i][0]["type2"])
            

    min_aev = 0
    min_cev = 0
    return min_aev, min_cev

def compare_attack():
    return

def compare_spacial_attack(s_copy, ev_c, my_pokemon_bs_c, opposite_pokemon_ev_h, opposite_pokemon_bs_h, opposite_pokemon_ev_d, opposite_pokemon_bs_d, attack_move_power, attack_move_type, my_pokemon_type1, my_pokemon_type2, opposite_pokemon_type1, opposite_pokemon_type2):
    # 自ポケモンの攻撃力を計算
    my_pokemon_status_c = calculate.calculate_hpother(ev_c, my_pokemon_bs_c)

    # 敵ポケモンのHPを計算
    opposite_pokemon_status_h = calculate.calculate_hp(int(opposite_pokemon_ev_h), opposite_pokemon_bs_h)

    # 敵ポケモンの防御力を計算
    opposite_pokemon_status_d = calculate.calculate_hpother(int(opposite_pokemon_ev_d), opposite_pokemon_bs_d)

    # ポケモンに与えるダメージを計算
    damage = calculate.calculate_damage(attack_move_power, attack_move_type, my_pokemon_type1, my_pokemon_type2, opposite_pokemon_type1, opposite_pokemon_type2, my_pokemon_status_c, opposite_pokemon_status_d)

    # 条件を追加
    s_copy.add(opposite_pokemon_status_h - damage <= 0)