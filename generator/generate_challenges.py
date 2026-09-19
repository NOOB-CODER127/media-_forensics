#!/usr/bin/env python3
"""
Media Forensics & Deepfake Lab - Challenge Generator Engine (Updated)
Generates 3 progressive forensic challenges:
  1. Easy: Audio Forensics & Spectrogram Steganography (Operation Whispering Wiretap)
  2. Medium: Video Forensics & License Plate De-blur (Operation Ghost Vehicle)
  3. Hard: Image Forensics & Error Level Analysis on Crime Scene (Case 1: The Staged Crime Scene)
"""

import os
import io
import math
import struct
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
from scipy.signal import convolve2d, istft, spectrogram
import wave

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH1_DIR = os.path.join(BASE_DIR, "challenges", "challenge1_audio")
CH2_DIR = os.path.join(BASE_DIR, "challenges", "challenge2_video")
CH3_DIR = os.path.join(BASE_DIR, "challenges", "challenge3_ela")
ORIGINAL_CRIME_SCENE = os.path.join(BASE_DIR, "Case-1-dead-body-and-crime-scene-at-the-finding.webp")

# Fonts
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def get_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

# -------------------------------------------------------------------------
# CHALLENGE 1 (EASY): Audio Forensics (Spectrogram Steganography)
# -------------------------------------------------------------------------
def generate_challenge_1():
    print("[*] Generating Challenge 1 [EASY] (Audio Forensics & Spectrogram)...")
    os.makedirs(CH1_DIR, exist_ok=True)
    sol_dir = os.path.join(CH1_DIR, "solution")
    os.makedirs(sol_dir, exist_ok=True)

    sr = 44100
    duration = 16.0  # seconds
    nperseg = 1024
    noverlap = 512
    n_freqs = nperseg // 2 + 1
    total_samples = int(sr * duration)
    n_times = int(math.ceil((total_samples - noverlap) / (nperseg - noverlap)))

    # Flag message to encode in the spectrogram
    flag_text = "FLAG{SP3CTR4L_AUD10_CYPH3R}"

    # Render flag text as a crisp bitmap with measured bounds
    bmp_w = 640
    bmp_h = 50
    text_img = Image.new("L", (bmp_w, bmp_h), color=0)
    tdraw = ImageDraw.Draw(text_img)
    font_spec = get_font(FONT_BOLD, 24)
    tdraw.text((15, 8), flag_text, font=font_spec, fill=255)
    tdraw.rectangle([(2, 2), (bmp_w - 3, bmp_h - 3)], outline=200, width=2)
    text_arr = np.array(text_img, dtype=np.float32) / 255.0

    # Target Frequency Band: 9,000 Hz to 14,500 Hz
    freq_resolution = sr / float(nperseg)
    f_min, f_max = 9000.0, 14500.0
    bin_min = int(f_min / freq_resolution)
    bin_max = int(f_max / freq_resolution)
    target_bins = bin_max - bin_min

    # Time offset: 2.5s to 14.3s
    t_start_slice = int((2.5 * sr) / (nperseg - noverlap))
    t_end_slice = t_start_slice + int((11.8 * sr) / (nperseg - noverlap))
    target_time_slices = t_end_slice - t_start_slice

    resized_text = Image.fromarray((text_arr * 255).astype(np.uint8)).resize(
        (target_time_slices, target_bins), Image.Resampling.BILINEAR
    )
    resized_arr = np.array(resized_text, dtype=np.float32) / 255.0

    mag = np.zeros((n_freqs, n_times), dtype=np.float32)
    mag[bin_min:bin_max, t_start_slice:t_end_slice] = resized_arr[::-1, :] * 2.8

    # Realistic radio noise
    np.random.seed(1337)
    radio_noise = np.random.uniform(0.01, 0.04, mag.shape)
    for f_hum in [60, 120, 180, 1000, 2400]:
        hum_bin = int(f_hum / freq_resolution)
        if hum_bin < n_freqs:
            mag[hum_bin, :] += np.random.uniform(0.5, 1.2, n_times)

    total_mag = mag + radio_noise
    random_phases = np.random.uniform(0, 2 * np.pi, total_mag.shape)
    Zxx = total_mag * np.exp(1j * random_phases)
    _, audio_signal = istft(Zxx, fs=sr, nperseg=nperseg, noverlap=noverlap)

    audio_signal = audio_signal / (np.max(np.abs(audio_signal)) + 1e-6) * 0.85
    audio_int16 = (audio_signal * 32767).astype(np.int16)

    wav_path = os.path.join(CH1_DIR, "intercepted_wiretap.wav")
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(audio_int16.tobytes())
    print(f"  [+] Saved {wav_path}")

    # Reference spectrogram solution
    f_spec, t_spec, Sxx = spectrogram(audio_signal, sr, nperseg=nperseg, noverlap=noverlap)
    mask = f_spec <= 16000
    display_sxx = np.log10(Sxx[mask, :] + 1e-6)
    d_min, d_max = np.percentile(display_sxx, 15), np.percentile(display_sxx, 99.5)
    normalized = np.clip((display_sxx - d_min) / (d_max - d_min + 1e-6), 0, 1) * 255
    sol_img = Image.fromarray(normalized[::-1].astype(np.uint8))
    sol_img_path = os.path.join(sol_dir, "solution_spectrogram.png")
    sol_img.save(sol_img_path)
    print(f"  [+] Saved solution spectrogram {sol_img_path}")


# -------------------------------------------------------------------------
# CHALLENGE 2 (MEDIUM): Video Forensics (License Plate De-blur)
# -------------------------------------------------------------------------
def create_mjpeg_avi(frames, output_path, fps=20):
    width, height = frames[0].size
    frame_bytes = []
    for f in frames:
        buf = io.BytesIO()
        f.save(buf, format="JPEG", quality=85)
        b = buf.getvalue()
        if len(b) % 2 != 0:
            b += b"\x00"
        frame_bytes.append(b)

    num_frames = len(frame_bytes)
    us_per_frame = int(1_000_000 / fps)

    movi_chunks = bytearray()
    idx1_entries = bytearray()
    movi_offset = 4

    for b in frame_bytes:
        chunk_len = len(b)
        movi_chunks += b"00dc" + struct.pack("<I", chunk_len) + b
        idx1_entries += b"00dc" + struct.pack("<III", 0x10, movi_offset, chunk_len)
        movi_offset += 8 + chunk_len

    movi_data = b"movi" + bytes(movi_chunks)
    movi_list = b"LIST" + struct.pack("<I", len(movi_data)) + movi_data
    idx1_chunk = b"idx1" + struct.pack("<I", len(idx1_entries)) + bytes(idx1_entries)

    avih = struct.pack("<IIIIIIIIIIIIII",
        us_per_frame, 0, 0, 0x10, num_frames, 0, 1,
        max(len(b) for b in frame_bytes), width, height, 0, 0, 0, 0
    )
    avih_chunk = b"avih" + struct.pack("<I", len(avih)) + avih

    strh = struct.pack("<4s4sIIIIIIIIIIHH",
        b"vids", b"MJPG", 0, 0, 0, 1, fps, 0, num_frames,
        max(len(b) for b in frame_bytes), 0xFFFFFFFF, 0, 0, 0
    ) + struct.pack("<HH", width, height)
    strh_chunk = b"strh" + struct.pack("<I", len(strh)) + strh

    strf = struct.pack("<IIIHHIIIIII",
        40, width, height, 1, 24, struct.unpack("<I", b"MJPG")[0],
        width * height * 3, 0, 0, 0, 0
    )
    strf_chunk = b"strf" + struct.pack("<I", len(strf)) + strf

    hdrl_data = b"hdrl" + avih_chunk + b"LIST" + struct.pack("<I", len(b"strl" + strh_chunk + strf_chunk)) + b"strl" + strh_chunk + strf_chunk
    hdrl_list = b"LIST" + struct.pack("<I", len(hdrl_data)) + hdrl_data
    riff_data = b"AVI " + hdrl_list + movi_list + idx1_chunk
    riff_file = b"RIFF" + struct.pack("<I", len(riff_data)) + riff_data

    with open(output_path, "wb") as out_f:
        out_f.write(riff_file)

def generate_challenge_2():
    print("[*] Generating Challenge 2 [MEDIUM] (Video Forensics & License Plate De-blur)...")
    os.makedirs(CH2_DIR, exist_ok=True)
    frames_dir = os.path.join(CH2_DIR, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    sol_dir = os.path.join(CH2_DIR, "solution")
    os.makedirs(sol_dir, exist_ok=True)

    w, h = 800, 480
    num_frames = 80
    fps = 20

    plate_w, plate_h = 200, 70
    master_plate = Image.new("RGB", (plate_w, plate_h), color=(248, 250, 245))
    pdraw = ImageDraw.Draw(master_plate)
    pdraw.rectangle([(2, 2), (plate_w - 3, plate_h - 3)], outline=(20, 40, 110), width=3)
    pdraw.rectangle([(2, 2), (plate_w - 3, 18)], fill=(20, 40, 110))
    pdraw.text((55, 3), "NEW YORK", font=get_font(FONT_BOLD, 11), fill=(255, 255, 255))
    pdraw.text((16, 26), "NY-7842-FX", font=get_font(FONT_BOLD, 26), fill=(15, 18, 25))

    font_osd = get_font(FONT_MONO, 12)
    all_frames = []
    golden_frame_index = 44
    golden_crop_box = None

    for i in range(num_frames):
        frame = Image.new("RGB", (w, h), color=(18, 20, 24))
        fdraw = ImageDraw.Draw(frame)

        fdraw.polygon([(220, 160), (580, 160), (870, 480), (-70, 480)], fill=(30, 32, 36))
        for y_lane in range(180, 480, 45):
            scale_lane = (y_lane - 160) / 320.0
            lw = int(7 * scale_lane)
            lx = int(400 - (y_lane - 160) * 0.45)
            fdraw.rectangle([(lx - lw, y_lane), (lx + lw, y_lane + int(24 * scale_lane))], fill=(160, 140, 50))

        fdraw.ellipse([(640, 40), (740, 140)], fill=(180, 170, 130))
        for r_y in range(160, 480, 20):
            alpha = (r_y - 160) / 320.0
            fdraw.line([(670 - int(50*alpha), r_y), (710 + int(70*alpha), r_y)], fill=(45, 43, 36), width=2)

        if i < 44:
            s_param = (i / 44.0) ** 1.25 * 0.55
        else:
            s_param = 0.55 + ((i - 44.0) / 36.0) ** 1.65 * 0.45

        car_x = int(220 + s_param * 420)
        car_y = int(170 + s_param * 220)
        car_scale = 0.55 + s_param * 1.05

        cw = int(260 * car_scale)
        ch = int(130 * car_scale)
        c_left = car_x - cw // 2
        c_top = car_y - ch // 2

        fdraw.ellipse([(c_left - 10, c_top + ch - 15), (c_left + cw + 10, c_top + ch + 15)], fill=(10, 10, 12))
        fdraw.rounded_rectangle([(c_left, c_top + int(ch*0.3)), (c_left + cw, c_top + ch)], radius=8, fill=(38, 40, 45))
        fdraw.polygon([(c_left + int(cw*0.15), c_top + int(ch*0.3)),
                       (c_left + int(cw*0.3), c_top),
                       (c_left + int(cw*0.75), c_top),
                       (c_left + int(cw*0.85), c_top + int(ch*0.3))], fill=(24, 26, 32))
        fdraw.rounded_rectangle([(c_left + 8, c_top + int(ch*0.42)), (c_left + int(cw*0.18), c_top + int(ch*0.62))], radius=3, fill=(190, 30, 20))
        fdraw.rounded_rectangle([(c_left + int(cw*0.82), c_top + int(ch*0.42)), (c_left + cw - 8, c_top + int(ch*0.62))], radius=3, fill=(190, 30, 20))

        pw = int(plate_w * car_scale * 0.68)
        ph = int(plate_h * car_scale * 0.68)
        px = c_left + int(cw * 0.5) - pw // 2
        py = c_top + int(ch * 0.55)

        scaled_plate = master_plate.resize((max(20, pw), max(10, ph)), Image.Resampling.BILINEAR)

        if 42 <= i <= 46:
            blur_k = 6
            kernel = np.ones((1, blur_k), dtype=np.float32) / blur_k
            p_arr = np.array(scaled_plate, dtype=np.float32)
            b_arr = np.zeros_like(p_arr)
            for ch_idx in range(3):
                b_arr[:, :, ch_idx] = convolve2d(p_arr[:, :, ch_idx], kernel, mode="same", boundary="symm")
            noise = np.random.normal(0, 3.0, b_arr.shape)
            processed_plate = Image.fromarray(np.clip(b_arr + noise, 0, 255).astype(np.uint8))
            if i == golden_frame_index:
                golden_crop_box = (px - 15, py - 10, px + pw + 15, py + ph + 10)
        else:
            blur_k = max(14, int(26 * (1.0 if i > 46 else 0.85)))
            kernel = np.ones((1, blur_k), dtype=np.float32) / blur_k
            p_arr = np.array(scaled_plate, dtype=np.float32)
            b_arr = np.zeros_like(p_arr)
            for ch_idx in range(3):
                b_arr[:, :, ch_idx] = convolve2d(p_arr[:, :, ch_idx], kernel, mode="same", boundary="symm")
            noise = np.random.normal(0, 6.0, b_arr.shape)
            processed_plate = Image.fromarray(np.clip(b_arr + noise, 0, 255).astype(np.uint8))

        frame.paste(processed_plate, (px, py))

        ts_sec = 22 + (i // fps)
        ts_ms = int((i % fps) * (1000 / fps))
        osd_text = f"CAM-04 | 2026-09-18 02:41:{ts_sec:02d}.{ts_ms:03d} | METRO NORTH INTERSECTION | [REC]"
        fdraw.rectangle([(0, 0), (w, 28)], fill=(0, 0, 0))
        fdraw.text((15, 6), osd_text, font=font_osd, fill=(80, 220, 100))
        fdraw.text((w - 110, h - 22), f"FRAME #{i+1:03d}", font=font_osd, fill=(150, 150, 150))

        frame_filename = os.path.join(frames_dir, f"frame_{i+1:03d}.png")
        frame.save(frame_filename)
        all_frames.append(frame)

    avi_path = os.path.join(CH2_DIR, "traffic_surveillance.avi")
    create_mjpeg_avi(all_frames, avi_path, fps=fps)
    print(f"  [+] Saved {avi_path}")

    gif_path = os.path.join(CH2_DIR, "traffic_surveillance.gif")
    all_frames[0].save(gif_path, save_all=True, append_images=all_frames[1:], duration=50, loop=0)
    print(f"  [+] Saved {gif_path}")

    frame44 = all_frames[golden_frame_index]
    frame44.save(os.path.join(sol_dir, "golden_frame_045.png"))
    plate_crop = frame44.crop(golden_crop_box)
    plate_crop.save(os.path.join(sol_dir, "plate_raw_blurred_crop.png"))

    sharpened = plate_crop.filter(ImageFilter.UnsharpMask(radius=2.5, percent=250, threshold=2))
    contrast_enh = ImageEnhance.Contrast(sharpened).enhance(1.8)
    contrast_enh.save(os.path.join(sol_dir, "plate_deblurred_solution.png"))
    print(f"  [+] Saved deblurred plate solution {os.path.join(sol_dir, 'plate_deblurred_solution.png')}")


# -------------------------------------------------------------------------
# CHALLENGE 3 (HARD): Image Forensics & ELA on Crime Scene
# -------------------------------------------------------------------------
def generate_challenge_3():
    print("[*] Generating Challenge 3 [HARD] (Crime Scene ELA Manipulation)...")
    os.makedirs(CH3_DIR, exist_ok=True)
    sol_dir = os.path.join(CH3_DIR, "solution")
    os.makedirs(sol_dir, exist_ok=True)

    if not os.path.exists(ORIGINAL_CRIME_SCENE):
        print(f"[-] ERROR: Source file {ORIGINAL_CRIME_SCENE} not found!")
        return

    orig = Image.open(ORIGINAL_CRIME_SCENE).convert("RGB")
    w, h = orig.size

    # 1. Establish baseline JPEG compression for the room: Quality = 75
    buf_base = io.BytesIO()
    orig.save(buf_base, format="JPEG", quality=75)
    buf_base.seek(0)
    base_img = Image.open(buf_base).convert("RGB")

    # 2. Extract gun and surrounding blood region
    gun_box = (250, 490, 470, 615)
    gun_crop = orig.crop(gun_box)

    # 3. Add authentic forensic evidence tag next to the staged weapon
    card_w, card_h = 205, 26
    card = Image.new("RGB", (card_w, card_h), color=(244, 244, 238))
    cdraw = ImageDraw.Draw(card)
    cdraw.rectangle([(0, 0), (card_w - 1, card_h - 1)], outline=(40, 40, 40), width=1)
    font_mono = get_font(FONT_MONO, 8)
    cdraw.text((6, 3), "FORENSIC EVIDENCE TAG #01-W", font=font_mono, fill=(190, 25, 25))
    cdraw.text((6, 14), "ITEM: REVOLVER (.38 SPECIAL)", font=font_mono, fill=(35, 35, 35))

    gun_crop.paste(card, (5, 90))

    # Mask covering the gun body and the evidence tag with smooth boundary
    mask = Image.new("L", gun_crop.size, 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.polygon([(15, 40), (60, 10), (185, 40), (195, 65), (215, 90), (215, 120), (2, 120), (2, 75)], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(1.5))

    # 4. Composite tampered region onto the baseline room image
    tampered = base_img.copy()
    tampered.paste(gun_crop, gun_box, mask=mask)

    # 5. Save the challenge image at Quality 95 (creates the ELA error differential)
    output_crime_scene_jpg = os.path.join(CH3_DIR, "crime_scene_evidence.jpg")
    tampered.save(output_crime_scene_jpg, format="JPEG", quality=95)
    print(f"  [+] Saved {output_crime_scene_jpg}")

    # 6. Generate reference solution ELA image
    buf_resaved = io.BytesIO()
    tampered.save(buf_resaved, format="JPEG", quality=90)
    buf_resaved.seek(0)
    resaved = Image.open(buf_resaved).convert("RGB")

    diff = ImageChops.difference(tampered, resaved)
    ela_enhanced = ImageEnhance.Brightness(diff).enhance(30.0)
    ref_ela_path = os.path.join(sol_dir, "reference_crime_scene_ela.png")
    ela_enhanced.save(ref_ela_path)
    print(f"  [+] Saved reference ELA {ref_ela_path}")


def main():
    print("=" * 68)
    print(" MEDIA FORENSICS LAB - RECONFIGURED CHALLENGE GENERATION")
    print("=" * 68)
    generate_challenge_1()
    generate_challenge_2()
    generate_challenge_3()
    print("=" * 68)
    print("[✓] ALL 3 PROGRESSIVE CHALLENGES GENERATED SUCCESSFULLY!")
    print("=" * 68)

if __name__ == "__main__":
    main()
