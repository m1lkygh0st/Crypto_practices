from crypto_utils import ALPHABET, kasiski_test, decrypt_vigenere, evaluate_text


def v_11(raw_ciphertext, key_length, all_possible_keys):
    clean_cipher = "".join(c for c in raw_ciphertext.lower() if c in ALPHABET)

    print("\n")
    print("POINT 1: KAZISKI TEST")
    probable_lengths = kasiski_test(clean_cipher)
    if probable_lengths:
        print(f"Duplicate keys found! Most likely key lengths: {probable_lengths}")
    else:
        print("Kasiski's test found no repetitions")

    print("\n")
    print("STEP 2: COLLECTING THE DECRYPTION DATABASE")
    print(f"Generate and evaluate all possible keys of length {key_length}...")

    results = []
    for key_tuple in all_possible_keys:
        key_str = "".join(key_tuple)
        decrypted_text = decrypt_vigenere(raw_ciphertext.lower(), key_str)
        score = evaluate_text(decrypted_text)
        results.append({"key": key_str, "text": decrypted_text, "score": score})

    print(f"Done. Combinations generated: {len(results)}")
    print("The first 10 variants of not sorted list:")
    for res in results[:10]:
        print(f"[{res['key']}] -> {res['text'][:50]}...")

    print("\n")
    print("ITEM 3: DERIVE THE TOP 10 MOST LIKELY KEYS")
    results_sorted = sorted(results, key=lambda x: x["score"])
    for i, res in enumerate(results_sorted[:10], 1):
        print(f"{i}. Key: '{res['key'].upper()}' (Score: {res['score']:.2f})")
        print(f"   Text: {res['text'][:80]}...\n")


def v_12(raw_ciphertext, key_length, all_possible_keys):
    print("\n")
    print(f"STARTING TO OUTLINE ALL COMBINATIONS FOR LENGTH {key_length}")

    count = 0
    for key_tuple in all_possible_keys:
        key_str = "".join(key_tuple)
        decrypted_text = decrypt_vigenere(raw_ciphertext.lower(), key_str)
        print(f"[{key_str}] -> {decrypted_text}")
        count += 1

    print(f"\nDone! Total combinations displayed: {count}")
