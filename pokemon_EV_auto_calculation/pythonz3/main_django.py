from z3 import *
from . import calculate

def main(my_pokemon_bs, opposite_pokemon_bs, opposite_pokemon_ev, speed_list, attack_list, defense_list):
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

    if speed_list[0] == "y":
        compare_speed(s, my_pokemon_bs[0]["bs_s"], ev_s, opposite_pokemon_bs[0]["bs_s"], opposite_pokemon_ev["ev_s"])

    # 計算
    if s.check() == sat:
        # 解の表示
        m = s.model()
        ans_list = [m[ev_h], m[ev_a], m[ev_b], m[ev_c], m[ev_d], m[ev_s]]
        # 計算後の努力値を返す
        return ans_list
    else:
        ans_list = ["failed to solve"]
        return ans_list


# 関数に直してく
# 素早さの比較
def compare_speed(s, my_pokemon_bs_s, ev_s, opposite_pokemon_bs_s, opposite_pokemon_ev_s):
    # 自ポケモンの素早さを計算
    pokemon_me_stats_s = calculate.calculate_hpother(ev_s, my_pokemon_bs_s)

    # 敵ポケモンの素早さを計算
    pokemon_opposite1_stats_s = calculate.calculate_hpother(int(opposite_pokemon_ev_s), (opposite_pokemon_bs_s))

    # 条件を追加
    s.add(pokemon_me_stats_s > pokemon_opposite1_stats_s)