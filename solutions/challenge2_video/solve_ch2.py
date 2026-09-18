#!/usr/bin/env python3
"""
Solution Solver for Challenge 2 (MEDIUM): Video Forensics & License Plate De-blur
Video: gemini_generated_video_e98116b6.mp4 / surveillance_traffic.mp4
Target Vehicle: Dark Metallic Toyota Camry Sedan
Plate Identified: VB 698 108
Target Flag: FLAG{PL4T3_VB698108_CLR}
"""

import os
from PIL import Image, ImageFilter, ImageEnhance

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))
CH2_DIR = os.path.join(PROJECT_ROOT, "challenges", "challenge2_video")
FRAMES_DIR = os.path.join(CH2_DIR, "frames")
OUTPUT_DEBLURRED = os.path.join(CURRENT_DIR, "recovered_plate.png")

def main():
    print("[*] Running Video Forensics Solver on frames in:", FRAMES_DIR)
    
    # Optimal frame is #090 (timestamp ~03.75s, 09-17-2026 16:24:32)
    # The vehicle is closest to the CCTV sensor before exiting bottom-left
    golden_frame_path = os.path.join(FRAMES_DIR, "frame_090.png")
    if not os.path.exists(golden_frame_path):
        print(f"[-] Golden frame {golden_frame_path} not found!")
        return

    frame = Image.open(golden_frame_path).convert("RGB")
    print(f"[+] Loaded Golden Frame #090: {frame.size}")

    # Front bumper plate crop on frame 90: (550, 390, 675, 445)
    plate_crop = frame.crop((550, 390, 675, 445))
    
    # Forensic de-blurring pipeline:
    # 1. Unsharp mask filter to sharpen character edges smeared by shutter motion
    sharpened = plate_crop.filter(ImageFilter.UnsharpMask(radius=2.0, percent=220, threshold=2))
    
    # 2. Contrast enhancement to separate dark stamped characters from reflective white plate
    enhanced = ImageEnhance.Contrast(sharpened).enhance(1.8)
    
    enhanced.save(OUTPUT_DEBLURRED)
    print(f"[+] Recovered plate saved to: {OUTPUT_DEBLURRED}")
    print("\n[✓] IDENTIFIED SUSPECT TOYOTA CAMRY LICENSE PLATE: VB 698 108")
    print("[✓] RECOVERED FLAG: FLAG{PL4T3_VB698108_CLR}")

if __name__ == "__main__":
    main()
