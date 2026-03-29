"""File for code of decode hill cipher"""

import numpy as np
from decode_utils import format_matrix
from utils import text_to_numbers, pad_text, matrix_mod_inv

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = 26


def hill_known_plaintext_attack(plaintext, ciphertext, n):
    """Reconstructs the key K matrix of the Hill cipher"""
    p_nums = pad_text(text_to_numbers(plaintext), n)
    c_nums = pad_text(text_to_numbers(ciphertext), n)
    P = np.zeros((n, n), dtype=int)
    C = np.zeros((n, n), dtype=int)
    for i in range(n):
        P[:, i] = p_nums[i * n : (i + 1) * n]
        C[:, i] = c_nums[i * n : (i + 1) * n]
    P = np.mod(P, M).astype(int)
    C = np.mod(C, M).astype(int)
    print(f"\nMatrix of plaintext P ({n} * {n}):")
    print(format_matrix(P))
    print(f"Matrix of ciphertext C ({n} * {n}):")
    print(format_matrix(C))
    try:
        P_inv = matrix_mod_inv(P, M)
    except ValueError as exc:
        raise ValueError(
            "Matrix P is irreversible by mod 26\nTry a different plaintext type"
        ) from exc
    print(f"P ^ (-1) (mod {M}):")
    print(format_matrix(P_inv))
    K = np.mod(C @ P_inv, M).astype(int)
    print(f"Reconstructed key K = C · P ^ (-1) (mod {M}):")
    print(format_matrix(K))
    return K
