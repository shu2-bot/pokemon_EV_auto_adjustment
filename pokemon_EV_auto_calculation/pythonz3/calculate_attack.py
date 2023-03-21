from z3 import *
from . import calculate


def calculate_attack(s, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, min_sev):
    # ソルバーを複製
    s_copy = Solver()
    for c in s.assertions():
        s_copy.add(c)
    s_copy.add(ev_h == 0)
    s_copy.add(ev_b == 0)
    s_copy.add(ev_c == 0)
    s_copy.add(ev_d == 0)
    s_copy.add(ev_s == min_sev)

    # 攻撃が物理か特殊かで

    min_aev = 20
    return min_aev