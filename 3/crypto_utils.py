import string
from collections import Counter
import math

ENGLISH_FREQS = {
    "a": 0.08167,
    "b": 0.01492,
    "c": 0.02782,
    "d": 0.04253,
    "e": 0.12702,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.06966,
    "j": 0.00015,
    "k": 0.00772,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.05987,
    "s": 0.06327,
    "t": 0.09056,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.02360,
    "x": 0.00150,
    "y": 0.01974,
    "z": 0.00074,
}

ALPHABET = string.ascii_lowercase


def get_kasiski_distances(ciphertext, seq_len=3):
    distances = []
    for i in range(len(ciphertext) - seq_len):
        seq = ciphertext[i : i + seq_len]
        for j in range(i + seq_len, len(ciphertext) - seq_len):
            if ciphertext[j : j + seq_len] == seq:
                distances.append(j - i)
    return distances


def get_factors(number):
    factors = set()
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    factors.add(number)
    return factors


def kasiski_test(ciphertext, max_len=20):
    distances = get_kasiski_distances(ciphertext)
    if not distances:
        return []

    factor_counts = Counter()
    for dist in distances:
        for f in get_factors(dist):
            if 2 <= f <= max_len:
                factor_counts[f] += 1

    return [f[0] for f in factor_counts.most_common(5)]


def decrypt_vigenere(ciphertext, key):
    """Decryption with the correct counter (spaces do not confuse the key)"""
    plaintext = []
    key_len = len(key)
    key_index = 0
    for char in ciphertext:
        if char in ALPHABET:
            shift = ALPHABET.index(key[key_index % key_len])
            plain_char = ALPHABET[(ALPHABET.index(char) - shift) % 26]
            plaintext.append(plain_char)
            key_index += 1
        else:
            plaintext.append(char)
    return "".join(plaintext)


def evaluate_text(text):
    clean_text = "".join(c for c in text.lower() if c in ALPHABET)
    if not clean_text:
        return float("inf")

    freqs = Counter(clean_text)
    score = 0
    for char in ALPHABET:
        observed = freqs.get(char, 0)
        expected = len(clean_text) * ENGLISH_FREQS[char]
        if expected > 0:
            score += ((observed - expected) ** 2) / expected
    return score
