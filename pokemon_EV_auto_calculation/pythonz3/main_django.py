from z3 import *
from . import calculate_speed
from . import calculate_attack
from . import calculate_defense

def main(my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list, speed_list, attack_list, defense_list, move_type_category_power_list):
    # 自分のポケモンの努力値
    ev_h = Int("ev_h")
    ev_a = Int("ev_a")
    ev_b = Int("ev_b")
    ev_c = Int("ev_c")
    ev_d = Int("ev_d")
    ev_s = Int("ev_s")

    # ソルバーの作成
    s = Solver()

    # 努力値の条件
    set_option(precision = 10)
    s.add(0 <= ev_h, ev_h <= 252, ev_h % 4 == 0)
    s.add(0 <= ev_a, ev_a <= 252, ev_a % 4 == 0)
    s.add(0 <= ev_b, ev_b <= 252, ev_b % 4 == 0)
    s.add(0 <= ev_c, ev_c <= 252, ev_c % 4 == 0)
    s.add(0 <= ev_d, ev_d <= 252, ev_d % 4 == 0)
    s.add(0 <= ev_s, ev_s <= 252, ev_s % 4 == 0)
    s.add((ev_h + ev_a + ev_b + ev_c + ev_d + ev_s) <= 508)

    attack_move_sample = 100

    # 素早さの条件をソルバーに追加
    if "y" in speed_list:
        min_sev = calculate_speed.calculate_speed(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, speed_list, my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list)
    else:
        min_sev = 0
    s.add(ev_s == min_sev)
    
    # 攻撃と特殊攻撃の条件を追加
    if "y" in attack_list:
        attack_move_list = []
        for i in range(int(len(move_type_category_power_list)/2)):
            attack_move_list.append(move_type_category_power_list[i * 2])
            print('attack_move_list = ' + str(attack_move_list))
        min_aev, min_cev = calculate_attack.calculate_attack(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, min_sev, attack_list, attack_move_list, my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list)
    else:
        min_aev = 0
        min_cev = 0
    s.add(ev_a == min_aev)
    s.add(ev_c == min_cev)

    # 防御と特殊防御の条件を追加
    if "y" in defense_list:
        defense_move_list = []
        for i in range(int(len(move_type_category_power_list)/2)):
            defense_move_list.append(move_type_category_power_list[(i * 2) + 1])
            print('defense_move_list = ' + str(defense_move_list))
        min_hev, min_bev, min_dev = calculate_defense.calculate_defense(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, min_sev, min_aev, min_cev, defense_list, defense_move_list, my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list)
    else:
        min_hev = 0
        min_bev = 0
        min_dev = 0
    s.add(ev_h == min_hev)
    s.add(ev_b == min_bev)
    s.add(ev_d == min_dev)

    print('----------')
    print(min_hev, min_bev, min_dev)

    # 計算
    if s.check() == sat:
        # 解の表示
        m = s.model()
        ans_list = [m[ev_h], m[ev_a], m[ev_b], m[ev_c], m[ev_d], m[ev_s]]
        # 計算後の努力値を返す
        return ans_list
    else:
        ans_list = ["すまねえな、そんな都合のいい調整はないってよ"]
        return ans_list
