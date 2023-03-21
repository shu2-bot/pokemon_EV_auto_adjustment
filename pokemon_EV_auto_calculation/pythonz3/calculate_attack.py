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
            # s_copyに条件を追加
            compare_attack()
            compare_spacial_attack()
            

    min_aev = 0
    min_cev = 0
    return min_aev, min_cev

def compare_attack():
    return

def compare_spacial_attack():
    return