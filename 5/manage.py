"""Manage module"""

import os
import cv2

from utils import (
    generate_watermark_image,
    embed_watermark,
    extract_watermark,
    print_evaluation_block,
    jpeg_attack,
    calculate_ber,
    calculate_nc,
)


def fst():
    c_path = input("Введите путь к квадратному изображению-контейнеру: ")
    if not os.path.exists(c_path):
        print("Ошибка: Контейнер не найден")

    wm_text = input("Введите текст для водяного знака: ")
    wm_size_input = input("Введите размер матрицы водяного знака N: ")
    wm_size = int(wm_size_input) if wm_size_input.strip() else 128

    watermark_img = generate_watermark_image(wm_text, size=wm_size)

    k_input = input("Введите коэффициент k: ")
    k_val = float(k_input) if k_input.strip() else 20.0

    iter_input = input("Введите количество итераций Арнольда: ")
    iter_val = int(iter_input) if iter_input.strip() else 3

    print("\nВстраивание")
    watermarked, orig, orig_wm = embed_watermark(
        c_path, watermark_img, k=k_val, arnold_iter=iter_val
    )
    out_name = "watermarked_picture.png"
    cv2.imwrite(out_name, watermarked)
    print(f"Готово: сохранено как '{out_name}'")

    ext_wm_test = extract_watermark(
        orig, watermarked, orig_wm.shape[0], k=k_val, arnold_iter=iter_val
    )
    print_evaluation_block(orig, watermarked, orig_wm, ext_wm_test)


def snd():
    wm_path = input("Введите путь к изображению со встроенным ЦВЗ: ")
    orig_path = input("Введите путь к чистому исходному контейнеру: ")
    if not os.path.exists(wm_path) or not os.path.exists(orig_path):
        print("Ошибка: Файлы не найдены")

    n_input = input("Введите размер матрицы ЦВЗ N: ")
    n_val = int(n_input) if n_input.strip() else 128

    k_input = input("Введите коэффициент k: ")
    k_val = float(k_input) if k_input.strip() else 20.0

    iter_input = input("Введите количество итераций Арнольда: ")
    iter_val = int(iter_input) if iter_input.strip() else 3

    orig_img = cv2.imread(orig_path)
    watermarked_img = cv2.imread(wm_path)

    print("\nИзвлечение...")
    extracted_wm = extract_watermark(
        orig_img, watermarked_img, n_val, k=k_val, arnold_iter=iter_val
    )
    out_name = "extracted_watermark.png"
    cv2.imwrite(out_name, extracted_wm)
    print(f"Готово: текст извлечен и сохранен как '{out_name}'")


def frd():
    print("\nЗапуск экспериментов:")
    c_path = input("Введите путь к квадратному контейнеру: ")
    if not os.path.exists(c_path):
        print("Ошибка: Файл не найден")

    wm_text = input("Введите текст для знака: ")
    wm_size = 128
    watermark_img = generate_watermark_image(wm_text, size=wm_size)

    k_val = 20.0
    iter_val = 3

    watermarked, orig, orig_wm = embed_watermark(
        c_path, watermark_img, k=k_val, arnold_iter=iter_val
    )
    cv2.imwrite("test_watermarked.png", watermarked)
    N = orig_wm.shape[0]

    print("\n>>> ТЕСТ 1: БЕЗ АТАК")
    ext_no_attack = extract_watermark(
        orig, watermarked, N, k=k_val, arnold_iter=iter_val
    )
    cv2.imwrite("test_ext_no_attack.png", ext_no_attack)
    print_evaluation_block(orig, watermarked, orig_wm, ext_no_attack)

    print("\n>>> ТЕСТ 2: АТАКИ JPEG-СЖАТИЕМ")
    for q in [90, 70, 50, 30]:
        print(f"\n--- Качество JPEG: {q}% ---")
        attacked = jpeg_attack(watermarked, q)
        ext_jpeg = extract_watermark(orig, attacked, N, k=k_val, arnold_iter=iter_val)
        cv2.imwrite(f"test_ext_jpeg_{q}.png", ext_jpeg)

        ber_jpeg = calculate_ber(orig_wm, ext_jpeg)
        ncc_jpeg = calculate_nc(orig_wm, ext_jpeg)
        print(f"BER: {ber_jpeg:.4f}")
        print(f"NCC: {ncc_jpeg:.6f}")
