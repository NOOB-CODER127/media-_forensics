#!/usr/bin/env python3
"""
Media Forensics & Deepfake Lab - Generator for Additional Medium Challenges
Generates:
  - Challenge 4 (Medium ELA): Operation Rogue Credential (evidence_clearance_badge.jpg)
  - Challenge 5 (Medium Spectrogram): Operation Blackout Broadcast (covert_broadcast.wav)
"""

import os
import io
import math
import wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageEnhance
from scipy.signal import istft, spectrogram

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH4_DIR = os.path.join(BASE_DIR, "challenges", "challenge4_medium_ela")
CH5_DIR = os.path.join(BASE_DIR, "challenges", "challenge5_medium_audio")
SOL4_DIR = os.path.join(BASE_DIR, "solutions", "challenge4_medium_ela")
SOL5_DIR = os.path.join(BASE_DIR, "solutions", "challenge5_medium_audio")

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def get_font(path, sz):
    try:
        return ImageFont.truetype(path, sz)
    except Exception:
        return ImageFont.load_default()

# -------------------------------------------------------------------------
# CHALLENGE 4 (MEDIUM): Document Forensics & Error Level Analysis (ELA)
# -------------------------------------------------------------------------
def generate_challenge_4():
    print("[*] Generating Challenge 4 [MEDIUM] (Image ELA - Operation Rogue Credential)...")
    os.makedirs(CH4_DIR, exist_ok=True)
    os.makedirs(SOL4_DIR, exist_ok=True)

    w, h = 920, 620
    base = Image.new("RGB", (w, h), color=(243, 246, 250))
    draw = ImageDraw.Draw(base)

    # Subtle security guilloche / grid background
    for x in range(0, w, 20):
        draw.line([(x, 0), (x, h)], fill=(233, 237, 244), width=1)
    for y in range(0, h, 20):
        draw.line([(0, y), (w, y)], fill=(233, 237, 244), width=1)

    # Agency watermark seal in background
    draw.ellipse([(550, 140), (830, 420)], outline=(225, 231, 240), width=6)
    draw.ellipse([(570, 160), (810, 400)], outline=(225, 231, 240), width=2)

    # Top Header Banner
    draw.rectangle([(0, 0), (w, 90)], fill=(14, 28, 52))
    f_head = get_font(FONT_BOLD, 22)
    f_sub = get_font(FONT_MONO, 11)
    draw.text((30, 20), "FEDERAL FORENSICS & SECURITY ADMINISTRATION", fill=(255, 255, 255), font=f_head)
    draw.text((30, 54), "OFFICIAL BIOMETRIC CREDENTIAL // DIVISION OF SPECIAL ACCESS", fill=(0, 225, 255), font=f_sub)
    draw.line([(0, 90), (w, 90)], fill=(0, 200, 255), width=3)

    # Left Column: Photo Box
    draw.rectangle([(45, 125), (265, 385)], fill=(215, 225, 235), outline=(14, 28, 52), width=3)
    draw.ellipse([(105, 175), (205, 275)], fill=(75, 95, 125))  # Head
    draw.ellipse([(75, 285), (235, 435)], fill=(75, 95, 125))   # Torso
    draw.rectangle([(45, 355), (265, 385)], fill=(14, 28, 52))
    draw.text((80, 362), "ID: FA-90421-X", fill=(255, 255, 255), font=get_font(FONT_MONO, 13))

    # Barcode under photo
    bc_x = 45
    bc_y = 410
    draw.rectangle([(bc_x, bc_y), (bc_x + 220, bc_y + 60)], fill=(255, 255, 255), outline=(150, 160, 170), width=1)
    np.random.seed(42)
    curr_bx = bc_x + 10
    while curr_bx < bc_x + 210:
        bar_w = int(np.random.choice([2, 3, 5, 7]))
        draw.rectangle([(curr_bx, bc_y + 6), (curr_bx + bar_w, bc_y + 44)], fill=(10, 15, 25))
        curr_bx += bar_w + int(np.random.choice([2, 4, 6]))
    draw.text((bc_x + 35, bc_y + 46), "*90421-VANCE-A*", fill=(60, 60, 60), font=get_font(FONT_MONO, 10))

    # Security Chip Icon
    draw.rounded_rectangle([(45, 490), (115, 545)], radius=6, fill=(212, 175, 55), outline=(160, 130, 30), width=2)
    draw.rectangle([(65, 498), (95, 537)], outline=(140, 110, 20), width=1)
    draw.text((130, 505), "SEC-CHIP UID: 8841-A", fill=(100, 110, 125), font=get_font(FONT_MONO, 11))
    draw.text((130, 525), "HARDWARE TOKEN: HW_90421_OK", fill=(100, 110, 125), font=get_font(FONT_MONO, 10))

    # Right Column: Personal & Facility Information
    f_lbl = get_font(FONT_BOLD, 12)
    f_val = get_font(FONT_MONO, 14)
    draw.text((310, 125), "OPERATIVE NAME:", fill=(85, 95, 110), font=f_lbl)
    draw.text((310, 143), "ADRIAN VANCE  [TOKEN: OP_VANCE_90421]", fill=(14, 24, 42), font=f_val)

    draw.text((310, 175), "CREDENTIAL CLASSIFICATION:", fill=(85, 95, 110), font=f_lbl)
    draw.text((310, 193), "CLASS-B TECHNICAL CONTRACTOR", fill=(14, 24, 42), font=f_val)

    draw.text((310, 225), "ASSIGNED FACILITY SECTOR:", fill=(85, 95, 110), font=f_lbl)
    draw.text((310, 243), "SECTOR-4 EXTERIOR // GENERAL LABS  [CODE: SEC4_EXT_0994]", fill=(14, 24, 42), font=get_font(FONT_MONO, 12))

    draw.text((310, 275), "EXPIRATION & AUDIT:", fill=(85, 95, 110), font=f_lbl)
    draw.text((310, 293), "2028-11-30 // AUDIT: AUD_PASS_2028", fill=(14, 24, 42), font=get_font(FONT_MONO, 12))

    # Original Base Clearance Section (Level 1)
    draw.rectangle([(310, 335), (885, 555)], fill=(234, 239, 246), outline=(180, 190, 205), width=2)
    draw.text((330, 355), "CLEARANCE CLASSIFICATION: LEVEL 1 (RESTRICTED VISITOR)", fill=(100, 110, 125), font=get_font(FONT_BOLD, 14))
    draw.text((330, 385), "FACILITY ACCESS: RESTRICTED VISITOR PASS // ESCORT REQUIRED", fill=(110, 120, 135), font=get_font(FONT_MONO, 11))
    draw.text((330, 415), "SECURITY CLEARANCE TOKEN: VIS_LVL1_STANDARD", fill=(120, 130, 145), font=get_font(FONT_MONO, 11))

    # Bottom Document Footer
    draw.text((310, 580), "DOCUMENT SEC-889-V | DO NOT DUPLICATE | PROPERTY OF THE FEDERAL FORENSICS ADMIN", fill=(130, 140, 155), font=get_font(FONT_MONO, 9))

    # 1. Establish baseline JPEG compression (Quality = 70)
    buf_base = io.BytesIO()
    base.save(buf_base, format="JPEG", quality=70)
    buf_base.seek(0)
    base_q70 = Image.open(buf_base).convert("RGB")

    # 2. Render fraudulent clearance patch (Level 4 matching authentic style)
    patch_w = 575
    patch_h = 220
    patch = Image.new("RGB", (patch_w, patch_h), color=(234, 239, 246))
    pdraw = ImageDraw.Draw(patch)
    pdraw.rectangle([(0, 0), (patch_w - 1, patch_h - 1)], outline=(180, 190, 205), width=2)

    pdraw.text((20, 20), "CLEARANCE CLASSIFICATION: LEVEL 4 (TOP SECRET / SCI)", fill=(14, 28, 52), font=get_font(FONT_BOLD, 14))
    pdraw.text((20, 50), "FACILITY ACCESS: ALL RESTRICTED VAULTS & ARCHIVES GRANTED", fill=(14, 28, 52), font=get_font(FONT_MONO, 11))
    pdraw.text((20, 80), "SECURITY CLEARANCE TOKEN: CL34R4NC3_0V3RR1D3", fill=(14, 28, 52), font=get_font(FONT_MONO, 12))
    pdraw.text((20, 110), "SPECIAL ACCESS PROGRAM: PROJECT CERBERUS [VAULT 04]", fill=(14, 28, 52), font=get_font(FONT_MONO, 11))
    pdraw.text((20, 140), "DIGITAL AUTHENTICATION: #SEC-90421-CERBERUS-VALID", fill=(100, 110, 125), font=get_font(FONT_MONO, 10))

    # 3. Paste fraudulent patch onto base
    composite = base_q70.copy()
    composite.paste(patch, (310, 335))

    # 4. Save final challenge image as scanned JPEG at Quality = 95
    out_badge = os.path.join(CH4_DIR, "evidence_clearance_badge.jpg")
    composite.save(out_badge, format="JPEG", quality=95)
    print(f"  [+] Saved {out_badge}")

    # 5. Generate reference solution ELA image
    buf_ela = io.BytesIO()
    composite.save(buf_ela, format="JPEG", quality=90)
    buf_ela.seek(0)
    resaved = Image.open(buf_ela).convert("RGB")

    diff = ImageChops.difference(composite, resaved)
    ela_enhanced = ImageEnhance.Brightness(diff).enhance(30.0)
    ref_ela = os.path.join(SOL4_DIR, "reference_badge_ela.png")
    ela_enhanced.save(ref_ela)
    sol_master_badge = os.path.join(BASE_DIR, "solutions", "challenge4_medium_ela", "recovered_badge_ela.png")
    if os.path.exists(os.path.dirname(sol_master_badge)):
        ela_enhanced.save(sol_master_badge)
    print(f"  [+] Saved reference ELA {ref_ela}")


# -------------------------------------------------------------------------
# CHALLENGE 5 (MEDIUM): Stereo Audio Spectrogram (Operation Blackout Broadcast)
# -------------------------------------------------------------------------
def generate_challenge_5():
    print("[*] Generating Challenge 5 [MEDIUM] (Stereo Spectrogram - Operation Blackout Broadcast)...")
    os.makedirs(CH5_DIR, exist_ok=True)
    os.makedirs(SOL5_DIR, exist_ok=True)

    sr = 44100
    duration = 18.0
    nperseg = 1024
    noverlap = 512
    n_freqs = nperseg // 2 + 1
    total_samples = int(sr * duration)
    n_times = int(math.ceil((total_samples - noverlap) / (nperseg - noverlap)))

    # High-legibility frequency band: 6,000 Hz to 12,000 Hz
    f_min, f_max = 6000.0, 12000.0
    freq_res = sr / float(nperseg)
    bin_min = int(f_min / freq_res)
    bin_max = int(f_max / freq_res)
    target_bins = bin_max - bin_min

    # Time window: 2.2s to 15.8s
    t_start_slice = int((2.2 * sr) / (nperseg - noverlap))
    t_end_slice = t_start_slice + int((13.6 * sr) / (nperseg - noverlap))
    target_time_slices = t_end_slice - t_start_slice

    font_spec = get_font(FONT_BOLD, 26)

    def synthesize_channel(text_label, seed_val):
        np.random.seed(seed_val)
        bmp_w = 680
        bmp_h = 56
        text_img = Image.new("L", (bmp_w, bmp_h), color=0)
        tdraw = ImageDraw.Draw(text_img)
        tdraw.text((15, 10), text_label, font=font_spec, fill=255)
        tdraw.rectangle([(2, 2), (bmp_w - 3, bmp_h - 3)], outline=200, width=2)
        text_arr = np.array(text_img, dtype=np.float32) / 255.0

        resized = Image.fromarray((text_arr * 255).astype(np.uint8)).resize(
            (target_time_slices, target_bins), Image.Resampling.BILINEAR
        )
        resized_arr = np.array(resized, dtype=np.float32) / 255.0

        mag = np.zeros((n_freqs, n_times), dtype=np.float32)
        mag[bin_min:bin_max, t_start_slice:t_end_slice] = resized_arr[::-1, :] * 3.2

        # Ambient background synthesizer drone & harmonics
        for f_tone in [110, 220, 330, 440, 880, 1760]:
            b = int(f_tone / freq_res)
            if b < n_freqs:
                mag[b, :] += np.random.uniform(0.6, 1.3, n_times)

        noise = np.random.uniform(0.01, 0.04, mag.shape)
        total_mag = mag + noise
        phases = np.random.uniform(0, 2 * np.pi, total_mag.shape)
        _, sig = istft(total_mag * np.exp(1j * phases), fs=sr, nperseg=nperseg, noverlap=noverlap)
        sig = sig / (np.max(np.abs(sig)) + 1e-6) * 0.82
        return sig

    # Part 1 on Left, Part 2 on Right
    left_sig = synthesize_channel("FLAG{DU4L_CH4NN3L_", seed_val=101)
    right_sig = synthesize_channel("ST3R30_SP3CTRUM}", seed_val=202)

    min_len = min(len(left_sig), len(right_sig))
    left_sig = left_sig[:min_len]
    right_sig = right_sig[:min_len]

    # Interleave into 16-bit stereo PCM
    left_int16 = (left_sig * 32767).astype(np.int16)
    right_int16 = (right_sig * 32767).astype(np.int16)
    stereo_interleaved = np.empty((min_len * 2,), dtype=np.int16)
    stereo_interleaved[0::2] = left_int16
    stereo_interleaved[1::2] = right_int16

    wav_out = os.path.join(CH5_DIR, "covert_broadcast.wav")
    with wave.open(wav_out, "wb") as wf:
        wf.setnchannels(2)      # Stereo
        wf.setsampwidth(2)      # 16-bit
        wf.setframerate(sr)
        wf.writeframes(stereo_interleaved.tobytes())
    print(f"  [+] Saved stereo audio {wav_out}")

    # Generate reference solution spectrograms for both channels
    def render_spec(signal_arr, out_png):
        f_sp, t_sp, Sxx = spectrogram(signal_arr, sr, nperseg=nperseg, noverlap=noverlap)
        mask = f_sp <= 14000
        disp = np.log10(Sxx[mask, :] + 1e-6)
        d_min, d_max = np.percentile(disp, 15), np.percentile(disp, 99.5)
        norm = np.clip((disp - d_min) / (d_max - d_min + 1e-6), 0, 1) * 255
        img = Image.fromarray(norm[::-1].astype(np.uint8))
        img.save(out_png)

    render_spec(left_sig, os.path.join(SOL5_DIR, "solution_left_spectrogram.png"))
    render_spec(right_sig, os.path.join(SOL5_DIR, "solution_right_spectrogram.png"))
    print(f"  [+] Saved reference Left & Right spectrograms in {SOL5_DIR}")


if __name__ == "__main__":
    generate_challenge_4()
    generate_challenge_5()
    print("[✓] Additional Medium Challenges generated successfully!")
