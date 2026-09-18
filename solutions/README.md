# Media Forensics & Deepfake Lab — Solutions & Facilitator Key

> **CONFIDENTIAL // ORGANIZER & INSTRUCTOR USE ONLY**  
> This directory contains automated solvers, reference visual artifacts, and step-by-step walkthrough guides for all progressive challenges. Do NOT distribute this folder to workshop participants.

---

## 📋 Challenge Suite Overview

| Level | Challenge Name | Target File | Flag | Automated Solver |
| :---: | :--- | :--- | :--- | :--- |
| **Easy**<br>(30 min) | **Operation Whispering Wiretap** | `challenges/challenge1_audio/intercepted_wiretap.wav` | `FLAG{SP3CTR4L_AUD10_CYPH3R}` | `solutions/challenge1_audio/solve_ch1_audio.py` |
| **Medium**<br>(50 min) | **Operation Ghost Vehicle** | `challenges/challenge2_video/surveillance_traffic.mp4` *(or `frames/`)* | `FLAG{PL4T3_VB698108_CLR}`<br>*(or `VB 698 108`)* | `solutions/challenge2_video/solve_ch2.py` |
| **Hard**<br>(50 min) | **Case 1: The Staged Crime Scene** | `challenges/challenge3_ela/crime_scene_evidence.jpg` | `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}` | `solutions/challenge3_ela/solve_ch3_ela.py` |
| **Medium**<br>(50 min) | **Operation Rogue Credential** | `challenges/challenge4_medium_ela/evidence_clearance_badge.jpg` | `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}` | `solutions/challenge4_medium_ela/solve_ch4_ela.py` |
| **Medium**<br>(50 min) | **Operation Blackout Broadcast** | `challenges/challenge5_medium_audio/covert_broadcast.wav` | `FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}` | `solutions/challenge5_medium_audio/solve_ch5_audio.py` |

---

## 🧪 Verification Suite

To execute all five automated solver pipelines and assert flag correctness in one command:

```bash
python3 generator/verify_all.py
```

Expected Output:
```
========================================================================
 MEDIA FORENSICS LAB - AUTOMATED VERIFICATION SUITE
========================================================================

[*] Testing Challenge 1 [EASY]: Audio Forensics (Spectrogram)...
[✓] PASS: Expected flag 'FLAG{SP3CTR4L_AUD10_CYPH3R}' verified in output!

[*] Testing Challenge 2 [MEDIUM]: Video Forensics (De-blur)...
[✓] PASS: Expected flag 'FLAG{PL4T3_VB698108_CLR}' verified in output!

[*] Testing Challenge 3 [HARD]: Crime Scene Forensics (ELA)...
[✓] PASS: Expected flag 'FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}' verified in output!

[*] Testing Challenge 4 [MEDIUM]: Document Forensics (ELA)...
[✓] PASS: Expected flag 'FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}' verified in output!

[*] Testing Challenge 5 [MEDIUM]: Stereo Audio Forensics (Spatial Spectrogram)...
[✓] PASS: Expected flag 'FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}' verified in output!

========================================================================
[✓] ALL 5 FORENSIC CHALLENGES VERIFIED AND PASSING!
========================================================================
```

---

## 📂 Directory Contents

### `solutions/offline_ela_viewer.html`
- **Instructor ELA Tool**: Standalone HTML5/Canvas client-side Error Level Analysis inspector for quick facilitator live demonstration on a projector.

### `solutions/challenge1_audio/`
- **`solve_ch1_audio.py`**: Automated STFT spectrogram generation script that reads `intercepted_wiretap.wav` and renders `solution_spectrogram.png`.
- **`walkthrough.md`**: Facilitator guide with Audacity linear spectrogram settings.
- **`solution_spectrogram.png` / `spectrogram_output.png`**: Visual reference image showing the recovered wiretap cipher.

### `solutions/challenge2_video/`
- **`solve_ch2.py`**: Automated script that scans extracted frames, selects deceleration apex frame #090, crops the plate bounding box, applies unsharp mask de-blurring, and extracts the plate string.
- **`walkthrough.md`**: Motion deceleration physics and FFmpeg extraction facilitator walkthrough.
- **`golden_frame_090.png`**: Deceleration apex frame.
- **`plate_deblurred_solution.png`**: High-contrast unsharp masked plate output (`VB 698 108`).

### `solutions/challenge3_ela/`
- **`solve_ch3_ela.py`**: Re-compresses `crime_scene_evidence.jpg` at 90% JPEG quality, computes pixel difference, amplifies by 30x, and measures the 3.1x error level anomaly ratio on the staged revolver.
- **`walkthrough.md`**: Theoretical and practical forensic guide explaining how to distinguish natural edge response (cones A/B) from true areal recompression tampering using GIMP.
- **`reference_crime_scene_ela.png` / `crime_scene_ela_result.png`**: Reference ELA difference image highlighting the glowing staged revolver.

### `solutions/challenge4_medium_ela/`
- **`solve_ch4_ela.py`**: Re-compresses `evidence_clearance_badge.jpg` at 90% JPEG quality, computes pixel difference, amplifies by 30x, and detects the 16x compression anomaly ratio across the forged clearance rectangle.
- **`walkthrough.md`**: Step-by-step document forensics guide using GIMP (and instructor demonstration via `solutions/offline_ela_viewer.html`).
- **`reference_badge_ela.png` / `recovered_badge_ela.png`**: Reference ELA difference image highlighting the glowing forged clearance block.

### `solutions/challenge5_medium_audio/`
- **`solve_ch5_audio.py`**: Reads `covert_broadcast.wav`, separates Left and Right channels, computes STFT spectrograms across 5 kHz–13 kHz on each channel, and extracts both passkey halves.
- **`walkthrough.md`**: Step-by-step Audacity guide for decoupling stereo tracks (`Split Stereo Track`) to prevent frequency overlap.
- **`solution_left_spectrogram.png` / `recovered_left_spectrogram.png`**: Left channel spectrogram (`FLAG{DU4L_CH4NN3L_`).
- **`solution_right_spectrogram.png` / `recovered_right_spectrogram.png`**: Right channel spectrogram (`ST3R30_SP3CTRUM}`).
