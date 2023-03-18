from z3 import *
from . import calculate

def calculate_speed(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, speed_list, my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list):
        # ソルバーを複製
    s_copy = Solver()
    for c in s.assertions():
        s_copy.add(c)
    s_copy.add(ev_h == 0)
    s_copy.add(ev_a == 0)
    s_copy.add(ev_b == 0)
    s_copy.add(ev_c == 0)
    s_copy.add(ev_d == 0)

    # speedの条件を追加
    for i in range(len(speed_list)):
        if speed_list[i] == 'y':
            # opposite_pokemon_bs_listの中身が特殊なため, [i][0]["bs_s"]に[0]となっている
            compare_speed(s_copy, my_pokemon_bs[0]["bs_s"], ev_s, opposite_pokemon_bs_list[i][0]["bs_s"], opposite_pokemon_ev_list["ev_s"][i])

    # 解を探索
    min_sev = None
    while s_copy.check() == sat:
        # 解がある場合は、モデルを取得して表示します。
        m_copy = s_copy.model()
        sev_val = m_copy[ev_s].as_long()
        if (min_sev is None) or (sev_val < min_sev):
            min_sev = sev_val
        # 最後にチェックしたモデルを除外する制約条件を追加します。
        s_copy.add(Not(And(ev_s == m_copy[ev_s])))

    # 素早さの条件を取得
    print("min_sev = " + str(min_sev))
    return min_sev


def compare_speed(s, my_pokemon_bs_s, ev_s, opposite_pokemon_bs_s, opposite_pokemon_ev_s):
    # 自ポケモンの素早さを計算
    pokemon_me_stats_s = calculate.calculate_hpother(ev_s, my_pokemon_bs_s)

    # 敵ポケモンの素早さを計算
    pokemon_opposite1_stats_s = calculate.calculate_hpother(int(opposite_pokemon_ev_s), (opposite_pokemon_bs_s))

    # 条件を追加
    s.add(pokemon_me_stats_s > pokemon_opposite1_stats_s)