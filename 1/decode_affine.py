"""File: decode_affine.py"""

from math import gcd
import string


def decode_affine(input_ciphertext: str = "") -> str:
    """This function decodes affine cipher"""
    m = 26

    alp = dict(zip(string.ascii_uppercase, range(26)))
    alp_ = dict(zip(range(26), string.ascii_uppercase))

    freq_eng = [
        0.082,
        0.015,
        0.028,
        0.043,
        0.127,
        0.022,
        0.020,
        0.061,
        0.070,
        0.0016,
        0.0077,
        0.040,
        0.024,
        0.067,
        0.075,
        0.019,
        0.0012,
        0.060,
        0.063,
        0.091,
        0.028,
        0.0098,
        0.024,
        0.0015,
        0.02,
        0.00074,
    ]

    input_ind = []
    for c in input_ciphertext.upper():
        if "A" <= c <= "Z":
            input_ind.append(alp[c])
        elif c == " ":
            input_ind.append(" ")

    def similarity(ind=None) -> float:
        """This function returns the similarity"""
        cnt = [0] * 26
        total = len([ind_i for ind_i in ind if ind_i != " "])
        for ind_i in ind:
            if ind_i != " ":
                cnt[ind_i] += 1
        total_cnt = 0.0
        for i in range(26):
            if total > 0:
                freq_i = cnt[i] / total
            else:
                freq_i = 0
            total_cnt += abs(freq_i - freq_eng[i])
        return total_cnt

    valid_a = [a for a in range(1, m) if gcd(a, m) == 1]
    mn_similarity = 1
    mn_simtext = ""

    for a in valid_a:
        a_inv = pow(a, -1, m)
        for b in range(m):
            decrypted_ind = []
            for y in input_ind:
                if y == " ":
                    decrypted_ind.append(" ")
                else:
                    decrypted_ind.append((a_inv * (y - b)) % m)
            score = similarity(decrypted_ind)
            if score < mn_similarity:
                mn_similarity = score
                mn_simtext = ""
                for i in decrypted_ind:
                    if i != " ":
                        mn_simtext += alp_[i]
                    else:
                        mn_simtext += " "

    return mn_simtext
