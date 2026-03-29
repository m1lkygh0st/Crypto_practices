"""File for code of decode hill recur cipher"""

from itertools import product

import numpy as np

from decode_utils import format_matrix
from hill_recur import generate_keys
from utils import pad_text, text_to_numbers, matrix_mod_inv

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = 26


def blocks_from_text(nums, n):
    """Splits the list of numbers into blocks-columns of size n"""
    return [
        np.array(nums[i * n : (i + 1) * n], dtype=int) for i in range(len(nums) // n)
    ]


def solve_row(equations, n):
    """Solves a system of linear equations with the module of M"""
    if len(equations) >= n:
        A = np.zeros((len(equations), n), dtype=int)
        b = np.zeros(len(equations), dtype=int)
        for idx, (p_vec, c_val) in enumerate(equations):
            A[idx] = p_vec
            b[idx] = c_val
        A_sq = A[:n]
        b_sq = b[:n]
        try:
            A_inv = matrix_mod_inv(A_sq, M)
            row = np.mod(A_inv @ b_sq, M).astype(int)

            for p_vec, c_val in equations:
                if np.mod(np.dot(row, p_vec), M) != c_val:
                    return None
            return row
        except ValueError:
            pass

    if n <= 3:
        solutions = []
        for combo in product(range(M), repeat=n):
            k = np.array(combo, dtype=int)
            valid = True
            for p_vec, c_val in equations:
                if np.mod(np.dot(k, p_vec), M) != c_val:
                    valid = False
                    break
            if valid:
                solutions.append(k)
        return solutions if solutions else None
    return None


def recur_hill_known_plaintext_attack(plaintext, ciphertext, n):
    """Reconstructs K1 and K2 of the Hill recurrent cipher"""
    p_nums = pad_text(text_to_numbers(plaintext), n)
    c_nums = pad_text(text_to_numbers(ciphertext), n)

    num_blocks = len(p_nums) // n
    p_blocks = blocks_from_text(p_nums, n)
    c_blocks = blocks_from_text(c_nums, n)

    min_blocks = max(2 * n, 4)
    if num_blocks < min_blocks:
        raise ValueError(
            f"Not enough text: you need a minimum of {min_blocks} blocks "
            f"({min_blocks * n} characters), received {num_blocks} blocks"
        )

    print(f"\nTotal Blocks: {num_blocks}")
    print(f"Using blocks 0..{num_blocks - 1}")
    print("\nStep 1: Reconstruction of K1")
    print("From block 0: C0 = K1 * P0")
    print(f"P0 = {p_blocks[0]}")
    print(f"C0 = {c_blocks[0]}")

    k1_row_equations = []
    for i in range(n):
        k1_row_equations.append([(p_blocks[0], c_blocks[0][i])])

    print("\nStep 2: Reconstruction of K2")
    print("From block 1: C1 = K2 * P1")
    print(f"P1 = {p_blocks[1]}")
    print(f"C1 = {c_blocks[1]}")

    k2_row_equations = []
    for i in range(n):
        k2_row_equations.append([(p_blocks[1], c_blocks[1][i])])

    print(f"\nStep 3: brute force check on blocks 2..{num_blocks - 1}")

    k1_candidates = []
    for i in range(n):
        result = solve_row(k1_row_equations[i], n)
        if result is None:
            raise ValueError(f"K1 key string {i} could not be found")
        if isinstance(result, np.ndarray):
            k1_candidates.append([result])
        else:
            k1_candidates.append(result)

    k2_candidates = []
    for i in range(n):
        result = solve_row(k2_row_equations[i], n)
        if result is None:
            raise ValueError(f"K2 key string {i} could not be found")
        if isinstance(result, np.ndarray):
            k2_candidates.append([result])
        else:
            k2_candidates.append(result)

    print(
        f"Candidates K1: {' * '.join(str(len(c)) for c in k1_candidates)} "
        f"= {np.prod([len(c) for c in k1_candidates])} string combinations"
    )
    print(
        f"Candidates K2: {' * '.join(str(len(c)) for c in k2_candidates)} "
        f"= {np.prod([len(c) for c in k2_candidates])} string combinations"
    )

    found = False
    K1_result = None
    K2_result = None

    k1_row_combos = list(product(*k1_candidates))
    k2_row_combos = list(product(*k2_candidates))

    total = len(k1_row_combos) * len(k2_row_combos)
    print(f"Total combinations to check: {total}")

    for k1_rows in k1_row_combos:
        K1 = np.array(k1_rows, dtype=int)

        for k2_rows in k2_row_combos:
            K2 = np.array(k2_rows, dtype=int)

            try:
                keys = generate_keys(K1, K2, num_blocks)
            except ValueError, TypeError:
                continue

            valid = True
            for idx in range(2, num_blocks):
                c_check = np.mod(keys[idx] @ p_blocks[idx], M).astype(int)
                if not np.array_equal(c_check, c_blocks[idx]):
                    valid = False
                    break

            if valid:
                K1_result = K1
                K2_result = K2
                found = True
                break
        if found:
            break

    if not found:
        raise ValueError(
            "Could not find a suitable pair K1, K2\nTry a different plaintext set"
        )

    print("\nReconstructed key K1:")
    print(format_matrix(K1_result))
    print("Reconstructed key K2:")
    print(format_matrix(K2_result))

    print(f"Verification on all {num_blocks} blocks")
    keys = generate_keys(K1_result, K2_result, num_blocks)
    all_ok = True
    for i in range(num_blocks):
        c_check = np.mod(keys[i] @ p_blocks[i], M).astype(int)
        if not np.array_equal(c_check, c_blocks[i]):
            print(f"Block {i}: expected {c_blocks[i]}, got {c_check}")
            all_ok = False
    if all_ok:
        print(f"All {num_blocks} blocks are the same!")

    return K1_result, K2_result
