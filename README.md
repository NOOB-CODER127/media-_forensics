# Media Forensics & Deepfake Lab — Investigation Challenge Suite

> **Theme:** *"You are the digital forensic analyst – uncover the truth hidden in pixels, frames, and sound."*  
> **Target Audience:** 10–15 participants per batch (3 batches = 45 daily capacity)  
> **Session Length:** 3 Hours per batch  
> **Based on:** [media foren zone.pdf](file:///home/prab/med-for-cha/media%20foren%20zone.pdf)

---

## 📁 Repository Structure

```
med-for-cha/
├── Case-1-dead-body-and-crime-scene-at-the-finding.webp # Real crime scene source evidence
├── gemini_generated_video_e98116b6.mp4                 # Source 1080p surveillance video
├── media foren zone.pdf                                # Original event specification document
├── README.md                                           # Master documentation & quickstart
│
├── challenges/                                         # Participant Challenge Handouts (Zero Leaks)
│   ├── README.md                                       # Directory index & guide
│   ├── walkthrough.md                                  # Complete unified 5-challenge participant walkthrough
│   ├── challenge1_audio/                               # [EASY] Audio Forensics & Spectrogram
│   │   ├── intercepted_wiretap.wav                     # 16-second radio audio (16-bit 44.1kHz Mono)
│   │   ├── challenge1_brief.md                         # Case brief & attendee instructions
│   │   └── walkthrough.md                              # Audacity step-by-step participant walkthrough
│   │
│   ├── challenge2_video/                               # [MEDIUM] Video Forensics & License Plate De-blur
│   │   ├── surveillance_traffic.mp4                    # Real 1280x720 24fps traffic camera recording
│   │   ├── frames/                                     # Pre-extracted lossless PNG frames (#001 to #240)
│   │   ├── challenge2_brief.md                         # Case brief & attendee instructions
│   │   └── walkthrough.md                              # VLC & GIMP step-by-step participant walkthrough
│   │
│   ├── challenge3_ela/                                 # [HARD] Crime Scene Image Forensics & ELA
│   │   ├── crime_scene_evidence.jpg                    # Forensic crime scene photo with staged revolver
│   │   ├── challenge3_brief.md                         # Case 1 homicide investigation briefing
│   │   └── walkthrough.md                              # GIMP 5-step ELA participant walkthrough
│   │
│   ├── challenge4_medium_ela/                          # [MEDIUM] Document Forensics & ELA
│   │   ├── evidence_clearance_badge.jpg                # Security access ID badge with forged clearance
│   │   ├── challenge4_brief.md                         # Case brief & attendee instructions
│   │   └── walkthrough.md                              # GIMP document ELA participant walkthrough
│   │
│   └── challenge5_medium_audio/                        # [MEDIUM] Stereo Audio Forensics & Spatial Spectrogram
│       ├── covert_broadcast.wav                        # 18-second 44.1kHz Stereo audio recording
│       ├── challenge5_brief.md                         # Case brief & attendee instructions
│       └── walkthrough.md                              # Audacity stereo decoupling participant walkthrough
│
├── solutions/                                          # Top-Level Organizer Solutions (Confidential)
│   ├── README.md                                       # Facilitator answer keys & overview
│   ├── offline_ela_viewer.html                         # Instructor HTML5/Canvas ELA inspection tool
│   ├── challenge1_audio/                               # Audio solver & Audacity walkthrough
│   │   ├── solve_ch1_audio.py                          # Automated STFT python solver
│   │   ├── walkthrough.md                              # Facilitator guide
│   │   └── solution_spectrogram.png                    # Reference visual spectrogram
│   ├── challenge2_video/                               # Video solver & de-blur walkthrough
│   │   ├── solve_ch2.py                                # Automated plate unsharp-mask solver
│   │   ├── walkthrough.md                              # Deceleration frame analysis guide
│   │   ├── golden_frame_090.png                        # Deceleration Apex Frame #090
│   │   └── plate_deblurred_solution.png                # Enhanced plate result
│   ├── challenge3_ela/                                 # Crime scene ELA solver & analysis
│   │   ├── solve_ch3_ela.py                            # Automated ELA anomaly calculator
│   │   ├── walkthrough.md                              # Areal vs edge compression theory guide
│   │   └── reference_crime_scene_ela.png               # Reference glowing ELA difference map
│   ├── challenge4_medium_ela/                          # Document ELA solver & analysis
│   │   ├── solve_ch4_ela.py                            # Automated badge ELA solver
│   │   ├── walkthrough.md                              # Step-by-step document forensics guide
│   │   └── reference_badge_ela.png                     # Reference glowing ELA difference map
│   └── challenge5_medium_audio/                        # Stereo audio solver & analysis
│       ├── solve_ch5_audio.py                          # Automated stereo STFT solver
│       ├── walkthrough.md                              # Step-by-step channel decoupling guide
│       ├── solution_left_spectrogram.png               # Left channel spectrogram
│       └── solution_right_spectrogram.png              # Right channel spectrogram
│
├── generator/                                          # Generator & Automated Verification Suite
│   ├── generate_challenges.py                          # Primary challenge generator
│   ├── generate_new_challenges.py                      # Generator for additional Medium challenges
│   └── verify_all.py                                   # Automated 5-challenge headless verification suite
│
├── server/                                             # Local Distribution Portal
│   ├── run_server.py                                   # Offline HTTP server & zip packager
│   └── public/                                         # Dashboard, Web ELA tool, and downloads
│
└── handouts/                                           # Ready-to-Print Event Materials
    ├── Participant_Brief_and_CheatSheet.md             # Attendee reference & command cheatsheet
    ├── Batch_Score_Sheet.md                            # 15-participant tracking matrix for 3 batches
    └── Instructor_Guide_and_Timeline.md                # Facilitation playbook
```

---

## 🏆 Challenge Progression & Master Key

| Level | Challenge Name | Domain | Flag | Primary Forensic Technique |
| :---: | :--- | :--- | :--- | :--- |
| **Easy**<br>(30 min) | **Operation Whispering Wiretap** | Audio Forensics | `FLAG{SP3CTR4L_AUD10_CYPH3R}` | Short-Time Fourier Transform (Spectrogram) in 9kHz–14.5kHz band |
| **Medium**<br>(50 min) | **Operation Ghost Vehicle** | Video Forensics | `FLAG{PL4T3_VB698108_CLR}`<br>*(Plate: `VB 698 108`)* | Identifying deceleration Apex Frame #90 + Unsharp Masking filter |
| **Hard**<br>(50 min) | **Case 1: The Staged Crime Scene** | Image Forensics | `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}` | Complex scene Error Level Analysis (ELA); discriminating edge artifacts from areal tampering to expose staged weapon |
| **Medium**<br>(50 min) | **Operation Rogue Credential** | Document Forensics | `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}` | Error Level Analysis on ID badge; detecting 16x compression anomaly on forged Level 4 clearance block |
| **Medium**<br>(50 min) | **Operation Blackout Broadcast** | Stereo Audio Forensics | `FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}` | Multi-channel spatial audio decoupling; splitting stereo tracks in Audacity to read independent frequency streams |

---

## 🚀 Quick Start Guide

### 1. Launch the Local Portal for Participants
```bash
python3 server/run_server.py
```
- Automatically binds to your Wi-Fi/LAN IP address (e.g. `http://192.168.1.X:8000/`).
- Serves one-click zip downloads, the in-browser ELA viewer, and an offline SHA-256 flag validator.

### 2. Verify All Challenges (Automated Verification)
```bash
python3 generator/verify_all.py
```
*Validates that all three challenges execute their solver pipelines and return expected flags.*

### 3. Re-generate Challenges
```bash
python3 generator/generate_challenges.py
```

---

## 🖨️ Printable Facilitation Stationery
- **[Participant Walkthrough Guide](file:///home/prab/med-for-cha/handouts/Participant_Walkthrough_Guide.md):** Step-by-step attendee walkthroughs for all 5 challenges using Audacity, VLC, and GIMP (zero Python references).
- **[Participant Cheat Sheet](file:///home/prab/med-for-cha/handouts/Participant_Brief_and_CheatSheet.md):** Print 1 copy per attendee.
- **[Batch Score Sheet](file:///home/prab/med-for-cha/handouts/Batch_Score_Sheet.md):** Print 1 copy per batch (3 batches = 45 daily capacity).
- **[Instructor Facilitation Playbook](file:///home/prab/med-for-cha/handouts/Instructor_Guide_and_Timeline.md):** Timed hint ladders (@ 10m, 18m, 25m / 15m, 30m, 40m) and live demo talking points.
