#!/usr/bin/env python3
"""
Media Forensics & Deepfake Lab - Automated Suite Verification
Executes headless solvers for all 3 challenges and asserts correct flag extraction.
"""

import sys
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLVERS = [
    ("Challenge 1 [EASY]: Audio Forensics (Spectrogram)",
     os.path.join(BASE_DIR, "solutions", "challenge1_audio", "solve_ch1_audio.py"),
     "FLAG{SP3CTR4L_AUD10_CYPH3R}"),

    ("Challenge 2 [MEDIUM]: Video Forensics (De-blur)",
     os.path.join(BASE_DIR, "solutions", "challenge2_video", "solve_ch2.py"),
     "FLAG{PL4T3_VB698108_CLR}"),

    ("Challenge 3 [HARD]: Crime Scene Forensics (ELA)",
     os.path.join(BASE_DIR, "solutions", "challenge3_ela", "solve_ch3_ela.py"),
     "FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}"),

    ("Challenge 4 [MEDIUM]: Document Forensics (ELA)",
     os.path.join(BASE_DIR, "solutions", "challenge4_medium_ela", "solve_ch4_ela.py"),
     "FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}"),

    ("Challenge 5 [MEDIUM]: Stereo Audio Forensics (Spatial Spectrogram)",
     os.path.join(BASE_DIR, "solutions", "challenge5_medium_audio", "solve_ch5_audio.py"),
     "FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}"),
]

def main():
    print("=" * 72)
    print(" MEDIA FORENSICS LAB - AUTOMATED VERIFICATION SUITE")
    print("=" * 72)

    all_passed = True

    for name, script_path, expected_flag in SOLVERS:
        print(f"\n[*] Testing {name}...")
        if not os.path.exists(script_path):
            print(f"[-] ERROR: Solver script not found at {script_path}")
            all_passed = False
            continue

        res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"[-] Solver failed with exit code {res.returncode}")
            print(res.stderr)
            all_passed = False
            continue

        output = res.stdout
        if expected_flag in output:
            print(f"[✓] PASS: Expected flag '{expected_flag}' verified in output!")
        else:
            print(f"[-] FAIL: Expected flag '{expected_flag}' not found in output!")
            print(output)
            all_passed = False

    print("\n" + "=" * 72)
    if all_passed:
        print("[✓] ALL 5 FORENSIC CHALLENGES VERIFIED AND PASSING!")
    else:
        print("[-] SOME VERIFICATION TESTS FAILED.")
    print("=" * 72)

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
