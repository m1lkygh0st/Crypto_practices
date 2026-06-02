"""Utils module"""

import math

import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import structural_similarity as ssim


def text_to_bits(text):
    bytes_data = text.encode("utf-8")
    bits_str = "".join(f"{b:08b}" for b in bytes_data)
    return np.array([int(bit) for bit in bits_str])


def bits_to_text(bits):
    bit_str = "".join(bits.astype(str))
    bytes_list = [
        int(bit_str[i : i + 8], 2)
        for i in range(0, len(bit_str), 8)
        if len(bit_str[i : i + 8]) == 8
    ]
    return bytearray(bytes_list).decode("utf-8", errors="ignore")


def embed_qim(img_matrix, bit_array, q):
    if q % 2 != 0:
        raise ValueError("Шаг квантования q должен быть четным")

    stego_matrix = img_matrix.astype(np.float64).copy()
    blue_channel = stego_matrix[:, :, 2].flatten()

    n_bits = len(bit_array)
    if n_bits > len(blue_channel):
        raise ValueError("Сообщение слишком длинное для этого изображения")

    target_pixels = blue_channel[:n_bits]
    embedded_pixels = np.floor(target_pixels / q) * q + (q // 2) * bit_array

    blue_channel[:n_bits] = embedded_pixels
    blue_channel = np.clip(blue_channel, 0, 255)

    stego_matrix[:, :, 2] = blue_channel.reshape(
        img_matrix.shape[0], img_matrix.shape[1]
    )
    return stego_matrix.astype(np.uint8)


def extract_qim(stego_matrix, msg_length, q):
    blue_channel = stego_matrix[:, :, 2].flatten().astype(np.float64)
    target_pixels = blue_channel[:msg_length]

    p0 = np.floor(target_pixels / q) * q
    p1 = p0 + (q / 2)

    diff0 = np.abs(target_pixels - p0)
    diff1 = np.abs(target_pixels - p1)

    return np.where(diff0 < diff1, 0, 1)


def print_metrics(orig, stego, num_bits, original_bits=None, extracted_bits=None):
    mse = np.mean((orig.astype(np.float64) - stego.astype(np.float64)) ** 2)
    rmse = math.sqrt(mse)
    psnr = float("inf") if mse == 0 else 10 * math.log10((255.0**2) / mse)
    ssim_val = ssim(orig, stego, channel_axis=-1)
    ec = num_bits / (orig.shape[0] * orig.shape[1])

    if original_bits is not None and extracted_bits is not None:
        ber = (
            np.sum(original_bits != extracted_bits) / len(original_bits)
            if len(original_bits) > 0
            else 1
        )
        orig_float = original_bits.astype(np.float64)
        ext_float = extracted_bits.astype(np.float64)
        numerator = np.sum(orig_float * ext_float)
        denominator = np.sqrt(np.sum(orig_float**2)) * np.sqrt(np.sum(ext_float**2))
        ncc = numerator / denominator if denominator != 0 else 0
    else:
        ber = 0
        ncc = 0

    print("\nОценка эффективности:")
    print(f"Ёмкость (EC): {ec:.6f} bpp")
    print(f"MSE:          {mse:.4f}")
    print(f"RMSE:         {rmse:.4f}")
    print(f"PSNR:         {psnr:.2f} dB")
    print(f"SSIM:         {ssim_val:.4f}")
    print(f"BER:          {ber:.4f}")
    print(f"NCC:          {ncc:.6f}")


def plot_histograms(orig_arr, stego_arr):
    orig_blue = orig_arr[:, :, 2].flatten()
    stego_blue = stego_arr[:, :, 2].flatten()

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(orig_blue, bins=256, range=[0, 256], color="blue", alpha=0.7)
    plt.title("Оригинал (Синий канал)")

    plt.subplot(1, 2, 2)
    plt.hist(stego_blue, bins=256, range=[0, 256], color="red", alpha=0.7)
    plt.title("Стего (Синий канал)")
    plt.show()
