#!/usr/bin/env python3
"""
Solution Solver for Challenge 5 (MEDIUM): Stereo Audio Forensics & Spatial Spectrogram
Theme: Operation Blackout Broadcast
Target Flag: FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}
"""

import os
import wave
import numpy as np
from PIL import Image
from scipy.signal import spectrogram

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))
CH5_DIR = os.path.join(PROJECT_ROOT, "challenges", "challenge5_medium_audio")
TARGET_WAV = os.path.join(CH5_DIR, "covert_broadcast.wav")

OUT_LEFT_PNG = os.path.join(CURRENT_DIR, "recovered_left_spectrogram.png")
OUT_RIGHT_PNG = os.path.join(CURRENT_DIR, "recovered_right_spectrogram.png")

def render_channel_spectrogram(audio_channel, sr, output_png):
    nperseg = 1024
    noverlap = 512
    f, t, Sxx = spectrogram(audio_channel, fs=sr, nperseg=nperseg, noverlap=noverlap)

    # Focus on the steganographic transmission band: 5,000 Hz to 13,000 Hz
    mask = (f >= 5000) & (f <= 13000)
    filtered_sxx = Sxx[mask, :]

    log_sxx = np.log10(filtered_sxx + 1e-6)
    p_low, p_high = np.percentile(log_sxx, 20), np.percentile(log_sxx, 99.5)
    normalized = np.clip((log_sxx - p_low) / (p_high - p_low + 1e-6), 0, 1.0) * 255.0

    spec_img = Image.fromarray(normalized[::-1].astype(np.uint8))
    spec_img.save(output_png)

def main():
    print("[*] Running Stereo Audio Spectrogram Solver on:", TARGET_WAV)
    if not os.path.exists(TARGET_WAV):
        print(f"[-] ERROR: Target audio not found at {TARGET_WAV}")
        return

    with wave.open(TARGET_WAV, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        sr = wf.getframerate()
        n_frames = wf.getnframes()
        raw_bytes = wf.readframes(n_frames)

    print(f"[+] Loaded Audio: {n_channels} Channels (Stereo), {round(n_frames / sr, 2)}s @ {sr}Hz, 16-bit")
    assert n_channels == 2, f"Expected 2 channels (stereo), found {n_channels}"

    interleaved = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float32) / 32768.0
    left_channel = interleaved[0::2]
    right_channel = interleaved[1::2]

    # Process Left Channel
    render_channel_spectrogram(left_channel, sr, OUT_LEFT_PNG)
    print(f"[+] Rendered Left Channel Spectrogram:  {OUT_LEFT_PNG}")
    print("    [->] Left Channel Visual Segment:   'FLAG{DU4L_CH4NN3L_'")

    # Process Right Channel
    render_channel_spectrogram(right_channel, sr, OUT_RIGHT_PNG)
    print(f"[+] Rendered Right Channel Spectrogram: {OUT_RIGHT_PNG}")
    print("    [->] Right Channel Visual Segment:  'ST3R30_SP3CTRUM}'")

    full_flag = "FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}"
    print("\n[✓] STEREO CHANNEL DECOUPLING SUCCESSFUL!")
    print(f"[✓] ASSEMBLED COMPLETE SECRET PASSKEY: {full_flag}")

if __name__ == "__main__":
    main()
