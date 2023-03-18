from z3 import *
from . import calculate

def main(my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list, speed_list, attack_list, defense_list):
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
    s.add(ev_s == min_sev)

    """
    # speedの条件を追加
    for i in range(len(speed_list)):
        if speed_list[i] == 'y':
            # opposite_pokemon_bs_listの中身が特殊なため, [i][0]["bs_s"]に[0]となっている
            compare_speed(s, my_pokemon_bs[0]["bs_s"], ev_s, opposite_pokemon_bs_list[i][0]["bs_s"], opposite_pokemon_ev_list["ev_s"][i])
    """
    # attackの条件を追加
    # defenseの条件を追加

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


# 素早さの比較
"""
素早さだけ先に確定させて、
"""
def compare_speed(s, my_pokemon_bs_s, ev_s, opposite_pokemon_bs_s, opposite_pokemon_ev_s):
    # 自ポケモンの素早さを計算
    pokemon_me_stats_s = calculate.calculate_hpother(ev_s, my_pokemon_bs_s)

    # 敵ポケモンの素早さを計算
    pokemon_opposite1_stats_s = calculate.calculate_hpother(int(opposite_pokemon_ev_s), (opposite_pokemon_bs_s))

    # 条件を追加
    s.add(pokemon_me_stats_s > pokemon_opposite1_stats_s)

# 攻撃するとき
"""
技のDBを作成
名前　威力　タイプ　物理か特殊化


"""