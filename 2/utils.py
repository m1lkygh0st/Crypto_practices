"""File for utils of the encryption and decryption"""

import math

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = 26


def text_to_numbers(text):
    """Return list of chars from symbols in text"""
    return [alp.find(i.upper()) for i in text if i.upper() in alp]


def numbers_to_text(numbers):
    """Translate list of indexes to symbols"""
    return "".join(alp[i % m] for i in numbers)


def pad_text(numbers, n):
    """Add symbol X to a multiplicity of n"""
    r = len(numbers) % n
    if r != 0:
        numbers += [alp.index("X")] * (n - r)
    return numbers


def mod_inv(a, m=m):
    """The inverse element of a with module of m"""
    a = a % m
    if math.gcd(a, m) != 1:
        raise ValueError(f"Обратный элемент для {a} по модулю {m} не существует")

    def egcd(a, b):
        """An advanced Euclidean algorithm to find the greatest common divisor"""
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x

    _, x, _ = egcd(a, m)
    return x % m


def cofactor(matrix, i, j):
    """Algebraic complement of element (i, j)"""
    minor = [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]
    if len(minor) == 1:
        det_minor = minor[0][0]
    else:
        det_minor = determinant(minor)
    return ((-1) ** (i + j)) * det_minor


def determinant(matrix):
    """Calculating the matrix determinant"""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        det += (
            ((-1) ** j)
            * matrix[0][j]
            * determinant([row[:j] + row[j + 1 :] for row in matrix[1:]])
        )
    return det


def matrix_mod_inv(matrix, m=m):
    """Inverse matrix with module of m"""
    n = len(matrix)
    det = determinant(matrix)
    det_mod = det % m

    if math.gcd(det_mod, m) != 1:
        raise ValueError(
            f"Matrix is irreversible into Z_{m} (det={det_mod}, gcd({det_mod},{m}) != 1)"
        )

    det_inv = mod_inv(det_mod, m)

    adj = [[cofactor(matrix, i, j) for j in range(n)] for i in range(n)]

    # Транспонируем и умножаем на обратный элемент детерминанта
    adj_transpose = [[adj[j][i] for j in range(n)] for i in range(n)]
    return [[(det_inv * adj_transpose[i][j]) % m for j in range(n)] for i in range(n)]


def validate_key(matrix, name="K"):
    """Check the reversibility of the key matrix."""
    det = determinant(matrix) % m
    if math.gcd(det, m) != 1:
        raise ValueError(
            f"Matrix {name}: det={det}, gcd({det},{m}) != 1; the key is irreversible"
        )
    print(f"{name} is reversible into Z_{m} (det = {det})")


def input_matrix(name, size):
    """The input of the matrix"""
    print(f"Matrix {name} |{size} * {size}|:")
    rows = []
    for i in range(size):
        while True:
            try:
                row = list(map(int, input(f"String {i + 1}: ").split()))
                if len(row) != size:
                    print(f"Need {size} numbers")
                    continue
                rows.append(row)
                break
            except ValueError:
                print("Input the numbers with space")
    validate_key(rows, name)
    return rows
