from z3 import *
import calculate

def main():
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
    s.add(0 <= ev_h, ev_h <= 252, ev_h % 4 == 0)
    s.add(0 <= ev_a, ev_a <= 252, ev_a % 4 == 0)
    s.add(0 <= ev_b, ev_b <= 252, ev_b % 4 == 0)
    s.add(0 <= ev_c, ev_c <= 252, ev_c % 4 == 0)
    s.add(0 <= ev_d, ev_d <= 252, ev_d % 4 == 0)
    s.add(0 <= ev_s, ev_s <= 252, ev_s % 4 == 0)
    s.add((ev_h + ev_a + ev_b + ev_c + ev_d + ev_s) <= 508)

    attack_move_sample = 100

    # 計算後の努力値を返す
    return 0


# 関数に直してく
# 自ポケモンの素早さを計算
pokemon_me_stats_s = calculate.calculate_hpother(s_ev, pokemon_me_bs["s_bs"])

# 敵ポケモンの素早さを計算
pokemon_opposite1_stats_s = calculate.calculate_hpother(pokemon_opposite1_ev["s_ev"], pokemon_opposite1_bs["s_bs"])

# 条件を追加
s.add(pokemon_me_stats_s > pokemon_opposite1_stats_s)