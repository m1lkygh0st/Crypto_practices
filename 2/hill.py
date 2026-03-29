"""File for hill encryption and decryption"""

from utils import pad_text, text_to_numbers, numbers_to_text, matrix_mod_inv

m = 26


def hill_encrypt(text, key):
    """This function is used to encrypt text with hill cipher"""
    n = len(key)
    nums = pad_text(text_to_numbers(text), n)
    result = []
    for i in range(0, len(nums), n):
        block = nums[i : i + n]
        result.extend(
            [sum(key[j][k] * block[k] for k in range(n)) % m for j in range(n)]
        )
    return numbers_to_text(result)


def hill_decrypt(ciphertext, key):
    """This function is used to decrypt text with hill cipher"""
    n = len(key)
    nums = text_to_numbers(ciphertext)
    if len(nums) % n != 0:
        raise ValueError(f"The len of ciphertext % len of the block != 0 : ({n})")
    key_inv = matrix_mod_inv(key)
    result = []
    for i in range(0, len(nums), n):
        block = nums[i : i + n]
        result.extend(
            [sum(key_inv[j][k] * block[k] for k in range(n)) % m for j in range(n)]
        )
    return numbers_to_text(result)
