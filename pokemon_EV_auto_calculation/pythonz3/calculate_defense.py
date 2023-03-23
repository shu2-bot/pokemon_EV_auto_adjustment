from z3 import *
from . import calculate


def calculate_defense(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, min_sev, min_aev, min_cev, defense_list, defense_move_list, my_pokemon_bs, opposite_pokemon_bs_list, opposite_pokemon_ev_list):
    # ソルバーを複製
    s_copy = Solver()
    # sの制約をコピーに追加
    for c in s.assertions():
        s_copy.add(c)
    s_copy.add(ev_a == min_aev)
    s_copy.add(ev_c == min_cev)
    s_copy.add(ev_s == min_sev)

    for i in range(len(defense_list)):
        if defense_list[i] == "y":
            print(defense_move_list)
            if defense_move_list[i][0]["category"] == "physical":
                compare_defense(s_copy, ev_h, ev_b, my_pokemon_bs[0]["bs_h"], my_pokemon_bs[0]["bs_b"], opposite_pokemon_ev_list["ev_a"][i], opposite_pokemon_bs_list[i][0]["bs_a"], defense_move_list[i][0]["power"], defense_move_list[i][0]["type"], my_pokemon_bs[0]["type1"], my_pokemon_bs[0]["type2"], opposite_pokemon_bs_list[i][0]["type1"], opposite_pokemon_bs_list[i][0]["type2"])
            # s_copyに条件を追加
            elif defense_move_list[i][0]["category"] == "special":
                compare_spacial_defense(s_copy, ev_h, ev_d, my_pokemon_bs[0]["bs_h"], my_pokemon_bs[0]["bs_d"], opposite_pokemon_ev_list["ev_c"][i], opposite_pokemon_bs_list[i][0]["bs_c"], defense_move_list[i][0]["power"], defense_move_list[i][0]["type"], my_pokemon_bs[0]["type1"], my_pokemon_bs[0]["type2"], opposite_pokemon_bs_list[i][0]["type1"], opposite_pokemon_bs_list[i][0]["type2"])
    
    min_hev = None
    min_bev = None
    min_dev = None
    min_sum = None
    while s_copy.check() == sat:
        # 解がある場合は、モデルを取得して表示します。
        m_copy = s_copy.model()
        hev_val = m_copy[ev_h].as_long()
        bev_val = m_copy[ev_b].as_long()
        dev_val = m_copy[ev_d].as_long()
        sum_val = hev_val + bev_val + dev_val
        if (min_sum is None) or (sum_val < min_sum):
            print('sum_val = ' + str(sum_val))
            min_sum = sum_val
            min_hev = hev_val
            min_bev = bev_val
            min_dev = dev_val

            s_copy.add(And(ev_h <= m_copy[ev_h]))
            s_copy.add(And(ev_b <= m_copy[ev_b]))
            s_copy.add(And(ev_d <= m_copy[ev_d]))
        # 最後にチェックしたモデルを除外する制約条件を追加します。
        s_copy.add(Not(And(ev_h == m_copy[ev_h], ev_b == m_copy[ev_b], ev_d == m_copy[ev_d])))
        
        # これだとEVH＝0の時が1回しか回せない
        #s_copy.add(Not(And(ev_h <= m_copy[ev_h])))
        #s_copy.add(Not(And(ev_b <= m_copy[ev_b])))
        #s_copy.add(Not(And(ev_d <= m_copy[ev_d])))

        
        
        

    # 素早さの条件を取得
    print("min_hev = " + str(min_hev))
    print("min_bev = " + str(min_bev))
    print("min_dev = " + str(min_dev))
    return min_hev, min_bev, min_dev

# 防御の場合
def compare_defense(s_copy, ev_h, ev_b, my_pokemon_bs_h, my_pokemon_bs_b, opposite_pokemon_ev_a, opposite_pokemon_bs_a, defense_move_power, defense_move_type, my_pokemon_type1, my_pokemon_type2, opposite_pokemon_type1, opposite_pokemon_type2):
    # 自ポケモンの体力を計算
    my_pokemon_status_h = calculate.calculate_hp(ev_h, my_pokemon_bs_h)

    # 自ポケモンの防御力を計算
    my_pokemon_status_b = calculate.calculate_hpother(ev_b, my_pokemon_bs_b)

    # 敵ポケモンの攻撃力を計算
    opposite_pokemon_status_a = calculate.calculate_hpother(int(opposite_pokemon_ev_a), opposite_pokemon_bs_a)

    # ダメージ計算
    damage = calculate.calculate_damage(defense_move_power, defense_move_type, opposite_pokemon_type1, opposite_pokemon_type2, my_pokemon_type1, my_pokemon_type2, opposite_pokemon_status_a, my_pokemon_status_b)

    # 条件を追加
    s_copy.add(my_pokemon_status_h - damage > 0)

# 特殊攻撃の場合
def compare_spacial_defense(s_copy, ev_h, ev_d, my_pokemon_bs_h, my_pokemon_bs_d, opposite_pokemon_ev_c, opposite_pokemon_bs_c, defense_move_power, defense_move_type, my_pokemon_type1, my_pokemon_type2, opposite_pokemon_type1, opposite_pokemon_type2):
    # 自ポケモンの体力を計算
    my_pokemon_status_h = calculate.calculate_hp(ev_h, my_pokemon_bs_h)

    # 自ポケモンの防御力を計算
    my_pokemon_status_d = calculate.calculate_hpother(ev_d, my_pokemon_bs_d)

    # 敵ポケモンの攻撃力を計算
    opposite_pokemon_status_c = calculate.calculate_hpother(int(opposite_pokemon_ev_c), opposite_pokemon_bs_c)

    # ダメージ計算
    damage = calculate.calculate_damage(defense_move_power, defense_move_type, opposite_pokemon_type1, opposite_pokemon_type2, my_pokemon_type1, my_pokemon_type2, opposite_pokemon_status_c, my_pokemon_status_d)

    # 条件を追加
    s_copy.add(my_pokemon_status_h - damage > 0)