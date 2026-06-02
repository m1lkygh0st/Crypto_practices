"""Manage module"""

import os

import numpy as np
from PIL import Image, ImageEnhance

from utils import (
    text_to_bits,
    embed_qim,
    print_metrics,
    plot_histograms,
    extract_qim,
    bits_to_text,
)


def fst():
    in_file = input("Имя исходного изображения: ")
    if not os.path.exists(in_file):
        print("Файл не найден. Создаю тестовый input1.jpg...")
        Image.fromarray(np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)).save(
            "input1.jpg"
        )
        in_file = "input1.jpg"

    out_file = input("Имя для сохранения: ") or "stego.png"
    q = int(input("Шаг квантования q: ") or 16)
    text = input("Введите секретное сообщение: ")

    orig = np.array(Image.open(in_file).convert("RGB"))
    bits = text_to_bits(text)

    # Встраивание
    stego = embed_qim(orig, bits, q)
    Image.fromarray(stego).save(out_file)
    print(f"\nСообщение успешно встроено в {out_file}!")
    print(f"Параметры: шаг q = {q}, длина в битах = {len(bits)}")

    # Оценка
    print_metrics(orig, stego, len(bits))
    plot_histograms(orig, stego)


def snd():
    stego_file = input("Имя стегоизображения: ")
    q = int(input("Введите шаг квантования q, который использовался: "))
    msg_len = int(input("Введите длину сообщения в битах: "))

    try:
        stego = np.array(Image.open(stego_file).convert("RGB"))
        ext_bits = extract_qim(stego, msg_len, q)
        print(f"\nИзвлечённое сообщение: {bits_to_text(ext_bits)}")
    except Exception as e:
        print(f"Ошибка извлечения: {e}")


def frd():
    print("\n--- Тест на робатность ---")
    stego_file = input("Имя стегоизображения для искажения: ")
    try:
        img = Image.open(stego_file)
        # Сохраняем в JPEG
        jpeg_name = "stego_compressed.jpg"
        img.save(jpeg_name, format="JPEG", quality=80)
        print(f"Сжатая JPEG-копия сохранена как '{jpeg_name}'")

        # Меняем яркость
        bright_name = "stego_bright.png"
        ImageEnhance.Brightness(img).enhance(1.3).save(bright_name)
        print(f"Копия с измененной яркостью сохранена как '{bright_name}'")
        print("Теперь попробуй извлечь текст из этих новых файлов (Пункт 2 меню)!")
    except Exception as e:
        print(f"Ошибка: {e}")
