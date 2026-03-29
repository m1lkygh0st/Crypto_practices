"""This file is used to decode the hill command"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = 26


def format_matrix(matrix):
    """Format the matrix for beautiful output"""
    lines = []
    for row in matrix:
        lines.append("│ " + " ".join(f"{x:2d}" for x in row) + " │")
    return "\n".join(lines) + "\n"


def input_text(st):
    """Text input filtered only for letters A-Z"""
    text = input(st).strip().upper()
    filtered = "".join(c for c in text if c in ALPHABET)
    if not filtered:
        return None
    if len(filtered) != len(text):
        print(f"Only letters left: {filtered}")
    return filtered


def solve_key_from_block(p_block, c_block, n):
    """Form a list of equations"""
    equations = []
    for i in range(n):
        equations.append((p_block.copy(), c_block[i]))
    return equations
