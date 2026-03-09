"""File affine_common_data.py"""

def find_x(k: int) -> int:
    t, new_t, r, new_r = 0, 1, 26, k
    while new_r:
        t, new_t = new_t, t - (r // new_r) * new_t
        r, new_r = new_r, r - (r // new_r) * new_r
    return t % 26 if r == 1 else 0
