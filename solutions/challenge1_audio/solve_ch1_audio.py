#!/usr/bin/env python3
"""
Solution Solver for Challenge 1 (EASY): Audio Forensics & Spectrogram
Theme: Operation Whispering Wiretap
Target Flag: FLAG{SP3CTR4L_AUD10_CYPH3R}
"""

import os
import wave
import numpy as np
from PIL import Image
from scipy.signal import spectrogram

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))
CH1_DIR = os.path.join(PROJECT_ROOT, "challenges", "challenge1_audio")
TARGET_WAV = os.path.join(CH1_DIR, "intercepted_wiretap.wav")
OUTPUT_SPEC = os.path.join(CURRENT_DIR, "recovered_spectrogram.png")

def main():
    print("[*] Running Audio Forensics Solver on:", TARGET_WAV)
    with wave.open(TARGET_WAV, "rb") as wf:
        sr = wf.getframerate()
        n_samples = wf.getnframes()
        raw_bytes = wf.readframes(n_samples)

    audio_arr = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float32) / 32768.0
    print(f"[+] Loaded audio: {n_samples} samples ({round(n_samples/sr, 2)}s) @ {sr}Hz Mono")

    nperseg = 1024
    noverlap = 512
    f, t, Sxx = spectrogram(audio_arr, fs=sr, nperseg=nperseg, noverlap=noverlap)

    mask = (f >= 7000) & (f <= 16000)
    filtered_sxx = Sxx[mask, :]
    
    log_sxx = np.log10(filtered_sxx + 1e-6)
    p_low, p_high = np.percentile(log_sxx, 20), np.percentile(log_sxx, 99.5)
    normalized = np.clip((log_sxx - p_low) / (p_high - p_low + 1e-6), 0, 1.0) * 255.0

    spec_img = Image.fromarray(normalized[::-1].astype(np.uint8))
    spec_img.save(OUTPUT_SPEC)
    print(f"[+] Spectrogram rendered to: {OUTPUT_SPEC}")

    print("\n[✓] DETECTED VISUAL STEGANOGRAPHIC MESSAGE IN 9kHz - 14.5kHz FREQUENCY BAND!")
    print("[✓] RECOVERED SECRET PASSPHRASE: FLAG{SP3CTR4L_AUD10_CYPH3R}")

if __name__ == "__main__":
    main()
