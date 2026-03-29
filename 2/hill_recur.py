"""File for hill_recur encryption and decryption"""

from utils import pad_text, text_to_numbers, numbers_to_text, matrix_mod_inv

m = 26


def generate_keys(k1, k2, count):
    """This function is used to generate keys for hill_recur cipher"""
    keys = [k1, k2]
    for i in range(2, count):
        keys.append(
            [
                [
                    sum(keys[i - 1][j][k] * keys[i - 2][k][l] for k in range(len(k1)))
                    % m
                    for l in range(len(k1[0]))
                ]
                for j in range(len(k1))
            ]
        )
    return keys[:count]


def recur_hill_encrypt(text, k1, k2):
    """This function is used to encrypt text with hill_recur cipher"""
    n = len(k1)
    nums = pad_text(text_to_numbers(text), n)
    num_blocks = len(nums) // n
    keys = generate_keys(k1, k2, num_blocks)
    result = []
    for i in range(num_blocks):
        block = nums[i * n : (i + 1) * n]
        result.extend(
            [sum(keys[i][j][k] * block[k] for k in range(n)) % m for j in range(n)]
        )
    return numbers_to_text(result)


def recur_hill_decrypt(ciphertext, k1, k2):
    """This function is used to decrypt text with hill cipher"""
    n = len(k1)
    nums = text_to_numbers(ciphertext)
    if len(nums) % n != 0:
        raise ValueError(f"The len of ciphertext % len of the block != 0 : ({n})")
    num_blocks = len(nums) // n
    keys = generate_keys(k1, k2, num_blocks)
    result = []
    for i in range(num_blocks):
        block = nums[i * n : (i + 1) * n]
        key_inv = matrix_mod_inv(keys[i])
        result.extend(
            [sum(key_inv[j][k] * block[k] for k in range(n)) % m for j in range(n)]
        )
    return numbers_to_text(result)
