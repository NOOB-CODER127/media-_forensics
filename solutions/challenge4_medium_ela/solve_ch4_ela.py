#!/usr/bin/env python3
"""
Solution Solver for Challenge 4 (MEDIUM): Document Forensics & Error Level Analysis (ELA)
Case File: Operation Rogue Credential
Target Flag: FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
"""

import os
import io
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))
CH4_DIR = os.path.join(PROJECT_ROOT, "challenges", "challenge4_medium_ela")
TARGET_IMAGE = os.path.join(CH4_DIR, "evidence_clearance_badge.jpg")
OUTPUT_ELA = os.path.join(CURRENT_DIR, "recovered_badge_ela.png")

def run_ela(image_path, quality=90, scale=30.0):
    original = Image.open(image_path).convert("RGB")
    buffer = io.BytesIO()
    original.save(buffer, format="JPEG", quality=quality)
    buffer.seek(0)
    resaved = Image.open(buffer).convert("RGB")
    diff = ImageChops.difference(original, resaved)
    enhanced = ImageEnhance.Brightness(diff).enhance(scale)
    return original, enhanced, diff

def main():
    print("[*] Running Document ELA Solver on:", TARGET_IMAGE)
    if not os.path.exists(TARGET_IMAGE):
        print(f"[-] ERROR: Target image not found at {TARGET_IMAGE}")
        return

    orig, enhanced, diff = run_ela(TARGET_IMAGE)
    enhanced.save(OUTPUT_ELA)
    print(f"[+] ELA difference map saved to: {OUTPUT_ELA}")

    # Analyze error density
    diff_arr = np.mean(np.array(diff), axis=2)
    bg_error = np.mean(diff_arr[125:350, 50:265])
    patch_error = np.mean(diff_arr[350:560, 310:875])

    print(f"[*] Authentic ID / Photo region error: {bg_error:.3f}")
    print(f"[*] Spliced Clearance patch error:    {patch_error:.3f}")
    ratio = patch_error / (bg_error + 1e-5)
    print(f"[+] Compression Anomaly Ratio:        {ratio:.2f}x")

    if ratio > 2.5:
        print("\n[✓] FORENSIC CONFIRMATION: DIGITAL SPLICING EXPOSED ON SECURITY CLEARANCE BLOCK!")
        print("[✓] RECOVERED AUTH OVERRIDE TOKEN: FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}")
    else:
        print("[-] Anomaly ratio below forensic threshold.")

if __name__ == "__main__":
    main()
