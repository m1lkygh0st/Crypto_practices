from crypto_utils import ALPHABET, evaluate_text


def decrypt_autokey_1char(ciphertext, primer_char):
    """
    Decrypting a Vigenère key with a single-character initial key.
    Each decrypted letter becomes the key for the next.
    """
    plaintext = []
    current_key = primer_char.upper()

    for char in ciphertext.upper():
        if char in ALPHABET:
            c_idx = ALPHABET.index(char)
            k_idx = ALPHABET.index(current_key)

            p_idx = (c_idx - k_idx) % 26
            p_char = ALPHABET[p_idx]

            plaintext.append(p_char)
            current_key = p_char
        else:
            plaintext.append(char)

    return "".join(plaintext)


def v_22(ciphertext):

    results = []

    for primer in ALPHABET:
        decrypted_text = decrypt_autokey_1char(ciphertext, primer)
        score = evaluate_text(decrypted_text)
        results.append((score, primer, decrypted_text))

    results.sort(key=lambda x: x[0])

    print("\n[+] TOP 5 most probable interpretations:\n")
    for i, (score, primer, text) in enumerate(results[:5], 1):
        print(f"{i}. Starter key: '{primer}' (Score: {score:.2f})")
        print(f"   Text: {text[:100]}...\n")
