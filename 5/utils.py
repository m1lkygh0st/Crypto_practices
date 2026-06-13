"""Utils module"""

import cv2
import numpy as np
import pywt
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim


def arnold_transform(img, iterations):
    n = img.shape[0]
    res = img.copy()
    for _ in range(iterations):
        new_res = np.zeros_like(res)
        for i in range(n):
            for j in range(n):
                new_res[(i + j) % n, (i + 2 * j) % n] = res[i, j]
        res = new_res
    return res


def inverse_arnold_transform(img, iterations):
    n = img.shape[0]
    res = img.copy()
    for _ in range(iterations):
        new_res = np.zeros_like(res)
        for i in range(n):
            for j in range(n):
                new_res[(2 * i - j) % n, (-i + j) % n] = res[i, j]
        res = new_res
    return res


def generate_watermark_image(text, size=128):
    img = np.zeros((size, size), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2

    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]

    if text_size[0] > size - 10:
        font_scale = (size - 10) / text_size[0]
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]

    text_x = (size - text_size[0]) // 2
    text_y = (size + text_size[1]) // 2

    cv2.putText(img, text, (text_x, text_y), font, font_scale, 255, thickness)
    cv2.imwrite("generated_watermark.png", img)
    return img


def embed_watermark(container_path, watermark_img, k=20, arnold_iter=1):
    container = cv2.imread(container_path)
    is_color = len(container.shape) == 3

    if is_color:
        ycrcb = cv2.cvtColor(container, cv2.COLOR_BGR2YCrCb)
        working_channel, cr, cb = cv2.split(ycrcb)
        working_channel = working_channel.astype(np.float32)
    else:
        working_channel = container.astype(np.float32)

    _, watermark = cv2.threshold(watermark_img, 127, 1, cv2.THRESH_BINARY)
    watermark = watermark.astype(np.float32)
    N = watermark.shape[0]

    container_dct = cv2.dct(working_channel)
    coeffs2 = pywt.dwt2(container_dct, "haar")
    LL, (LH, HL, HH) = coeffs2
    subbands = [LL, HL, LH, HH]

    w_arnold = arnold_transform(watermark, arnold_iter)
    w_dct = cv2.dct(w_arnold)

    half_N = N // 2
    w_blocks = [
        w_dct[0:half_N, 0:half_N],
        w_dct[0:half_N, half_N:N],
        w_dct[half_N:N, 0:half_N],
        w_dct[half_N:N, half_N:N],
    ]

    for i in range(4):
        subbands[i][0:half_N, 0:half_N] += w_blocks[i] * k

    coeffs2_mod = (subbands[0], (subbands[2], subbands[1], subbands[3]))
    container_dct_mod = pywt.idwt2(coeffs2_mod, "haar")

    watermarked_channel = cv2.idct(container_dct_mod)
    watermarked_channel = np.clip(np.round(watermarked_channel), 0, 255).astype(
        np.uint8
    )

    if is_color:
        merged = cv2.merge([watermarked_channel, cr, cb])
        watermarked_img = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)
    else:
        watermarked_img = watermarked_channel

    return watermarked_img, container, watermark


def extract_watermark(original_img, watermarked_img, N, k=20, arnold_iter=1):
    if len(original_img.shape) == 3:
        orig_working = cv2.cvtColor(original_img, cv2.COLOR_BGR2YCrCb)[:, :, 0].astype(
            np.float32
        )
        wm_working = cv2.cvtColor(watermarked_img, cv2.COLOR_BGR2YCrCb)[:, :, 0].astype(
            np.float32
        )
    else:
        orig_working = original_img.astype(np.float32)
        wm_working = watermarked_img.astype(np.float32)

    orig_dct = cv2.dct(orig_working)
    orig_LL, (orig_LH, orig_HL, orig_HH) = pywt.dwt2(orig_dct, "haar")
    orig_subbands = [orig_LL, orig_HL, orig_LH, orig_HH]

    wm_dct = cv2.dct(wm_working)
    wm_LL, (wm_LH, wm_HL, wm_HH) = pywt.dwt2(wm_dct, "haar")
    wm_subbands = [wm_LL, wm_HL, wm_LH, wm_HH]

    half_N = N // 2
    w_blocks_ext = []

    for i in range(4):
        block = (
            wm_subbands[i][0:half_N, 0:half_N] - orig_subbands[i][0:half_N, 0:half_N]
        ) / k
        w_blocks_ext.append(block)

    w_dct_ext = np.zeros((N, N), dtype=np.float32)
    w_dct_ext[0:half_N, 0:half_N] = w_blocks_ext[0]
    w_dct_ext[0:half_N, half_N:N] = w_blocks_ext[1]
    w_dct_ext[half_N:N, 0:half_N] = w_blocks_ext[2]
    w_dct_ext[half_N:N, half_N:N] = w_blocks_ext[3]

    w_arnold_ext = cv2.idct(w_dct_ext)
    w_ext = inverse_arnold_transform(w_arnold_ext, arnold_iter)
    w_ext = np.where(w_ext > 0.5, 255, 0).astype(np.uint8)

    return w_ext


def jpeg_attack(img, quality):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, enc_img = cv2.imencode(".jpg", img, encode_param)
    dec_img = cv2.imdecode(enc_img, cv2.IMREAD_COLOR)
    return dec_img


def calculate_mse(orig, wm):
    return np.mean((orig.astype(np.float32) - wm.astype(np.float32)) ** 2)


def calculate_nc(orig_wm, ext_wm):
    o = np.where(orig_wm > 127, 1, 0).astype(np.float32)
    e = np.where(ext_wm > 127, 1, 0).astype(np.float32)
    numerator = np.sum(o * e)
    denominator = np.sqrt(np.sum(o**2) * np.sum(e**2))
    if denominator == 0:
        return 0.0
    return numerator / denominator


def calculate_ber(orig_wm, ext_wm):
    o = np.where(orig_wm > 127, 1, 0)
    e = np.where(ext_wm > 127, 1, 0)
    errors = np.sum(o != e)
    total_bits = o.size
    return errors / total_bits


def print_evaluation_block(orig_img, watermarked_img, orig_wm, ext_wm):
    """Выводит полный блок оценки эффективности"""
    mse_val = calculate_mse(orig_img, watermarked_img)
    rmse_val = np.sqrt(mse_val)

    if len(orig_img.shape) == 3:
        psnr_val = psnr(orig_img, watermarked_img)
        ssim_val = ssim(orig_img, watermarked_img, channel_axis=2)
    else:
        psnr_val = psnr(orig_img, watermarked_img)
        ssim_val = ssim(orig_img, watermarked_img)

    ec_val = (orig_wm.shape[0] * orig_wm.shape[1]) / (
        orig_img.shape[0] * orig_img.shape[1]
    )
    ber_val = calculate_ber(orig_wm, ext_wm)
    ncc_val = calculate_nc(orig_wm, ext_wm)

    print("\nОЦЕНКА ЭФФЕКТИВНОСТИ")
    print(f"Ёмкость (EC): {ec_val:.6f} bpp")
    print(f"MSE:          {mse_val:.4f}")
    print(f"RMSE:         {rmse_val:.4f}")
    print(f"PSNR:         {psnr_val:.2f} dB")
    print(f"SSIM:         {ssim_val:.4f}")
    print(f"BER:          {ber_val:.4f}")
    print(f"NCC:          {ncc_val:.6f}")
