"""File: decode_affine_recur.py"""

import math
import random


def char_to_num(c):
    return ord(c.upper()) - ord("A")


def num_to_char(n, original_char):
    return chr(n + ord("A")) if original_char.isupper() else chr(n + ord("A")).lower()


def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_recurrent_decrypt(text, a1, b1, a2, b2):
    if math.gcd(a1, 26) != 1 or math.gcd(a2, 26) != 1:
        return None

    res = []
    curr_a1, curr_b1 = a1, b1
    curr_a2, curr_b2 = a2, b2

    for i, ch in enumerate(text):
        if ch.isalpha():
            y = char_to_num(ch)
            if i == 0:
                a_i, b_i = curr_a1, curr_b1
            elif i == 1:
                a_i, b_i = curr_a2, curr_b2
            else:
                a_i = (curr_a2 * curr_a1) % 26
                b_i = (curr_b2 + curr_b1) % 26
                curr_a1, curr_b1 = curr_a2, curr_b2
                curr_a2, curr_b2 = a_i, b_i

            a_inv = mod_inverse(a_i)
            x = (a_inv * (y - b_i)) % 26
            res.append(num_to_char(x, ch))
        else:
            res.append(ch)

    return "".join(res)


def english_score(text):
    letters = [ch for ch in text.upper() if ch.isalpha()]
    common_bigrams = ["TH", "HE", "IN", "ER", "AN", "RE", "ON", "AT", "EN", "ND"]
    common_trigrams = ["THE", "AND", "ING", "HER", "ERE", "ENT", "THA", "NTH"]
    score = sum(3 * "".join(letters).count(bg) for bg in common_bigrams)
    score += sum(7 * "".join(letters).count(tg) for tg in common_trigrams)
    vowels_ratio = sum(1 for ch in letters if ch in "AEIOU") / len(letters)
    if 0.25 <= vowels_ratio <= 0.45:
        score += 10
    return score


def decode_affine_recur(text, max_trials=5000):
    valid_a = [a for a in range(1, 26) if math.gcd(a, 26) == 1]
    results = []
    for _ in range(max_trials):
        a1, a2 = random.choice(valid_a), random.choice(valid_a)
        b1, b2 = random.randint(0, 25), random.randint(0, 25)
        decrypted = affine_recurrent_decrypt(text, a1, b1, a2, b2)
        if decrypted:
            score = english_score(decrypted)
            results.append((score, decrypted))
    if not results:
        return None
    results.sort(reverse=True, key=lambda x: x[0])
    return results[0][1]
