# Media Forensics & Deepfake Lab — Instructor Facilitation Playbook

> **Role:** Zone Lead (Facilitator) & Lab Assistant  
> **Batch Duration:** 3 Hours (180 minutes)  
> **Batch Capacity:** 10 – 15 Participants  
> **Session Objective:** Immersive, hands-on forensics investigation training with three progressive real-world challenges.

---

## 1. Setup Checklist (30 Minutes Before Batch 1)
- [ ] Connect Zone Laptop to venue projector / large monitor.
- [ ] Connect Zone Laptop to local Wi-Fi or configure portable mobile hotspot.
- [ ] Launch local HTTP distribution server:
  ```bash
  python3 server/run_server.py
  ```
- [ ] Project the server IP / URL (e.g., `http://192.168.1.50:8000`) and Wi-Fi credentials on screen.
- [ ] Ensure backup laptop is booted with identical files.
- [ ] Lay out printed **Participant Cheat Sheets**, **Score Sheets**, and **Prize Tokens / Candies**.

---

## 2. Session Timeline & Phase Flow

| Timeline | Phase | Activity & Instructor Role |
| :--- | :--- | :--- |
| **0:00 – 0:15** | Arrival & Setup | Connect to Wi-Fi, download challenge suite from portal |
| **0:15 – 0:25** | Demo 1 | **Live Demo:** Audio Spectrogram Steganography principles & Audacity |
| **0:25 – 0:55** | **Challenge 1 (Easy)** | **Solve Operation Whispering Wiretap (Audio - 30 mins)** |
| **0:55 – 1:05** | Solution 1 & Demo 2 | Reveal Ch 1, **Live Demo:** Video frame extraction & Unsharp Masking |
| **1:05 – 1:55** | **Challenge 2 (Medium)** | **Solve Operation Ghost Vehicle (Video CCTV - 50 mins)** |
| **1:55 – 2:05** | Solution 2 & Demo 3 | Reveal Ch 2, **Live Demo:** Advanced Error Level Analysis (ELA) on crime scenes |
| **2:05 – 2:55** | **Challenge 3 (Hard)** | **Solve Case 1: The Staged Crime Scene (Crime Scene ELA - 50 mins)** |
| **2:55 – 3:00** | Awards & Wrap-Up | Final score reconciliation, token award ceremony, Q&A |

---

### Phase 1: Welcome & Setup (0:00 – 0:15 | 15 mins)
- **What You Say:**
  > *"Welcome agents to the Media Forensics & Deepfake Lab. In this lab, you are digital forensic analysts investigating manipulated media across three domains: sound frequencies, video surveillance, and crime scene photographs. You will solve three progressive case files today."*
- **Action:**
  - Instruct participants to connect to the zone Wi-Fi.
  - Have them browse to `http://<IP>:8000` and click **"Download Challenge Suite"** (or individual folders).
  - Verify every participant has the files extracted and can open the briefs.

---

### Phase 2: Challenge 1 — Audio Spectrogram (0:15 – 0:55 | 40 mins)
- **Live Demo (0:15 – 0:25 | 10 mins):**
  - Sound is not just a 1D wave of pressure over time; it is a composition of frequencies. Steganographers hide visual text inside frequencies above human speech (8 kHz – 16 kHz) so that it sounds like random static, but looks like clear text when viewed through a spectrogram.
  - Open Audacity, switch to **Spectrogram** view, and show where **Linear Scale** is selected in **Spectrogram Settings**.
- **Hands-On Solving (0:25 – 0:55 | 30 mins):**
  - Participants inspect `intercepted_wiretap.wav`.
  - **Timed Hint Ladder:**
    - **@ 10 mins (0:35):** *"Do not rely on your headphones. Open the file in Audacity or Sonic Visualiser and switch from Waveform to Spectrogram view."*
    - **@ 18 mins (0:43):** *"If the text looks squished against the top of the track, change your Spectrogram Scale from Logarithmic to 'Linear' in Spectrogram Settings."*
    - **@ 25 mins (0:50):** *"Look between seconds 2.5 and 14.5 in the 9,000 Hz to 14,000 Hz band for the white framed flag box."*
  - **Verification & Prize:**
    - Flag: `FLAG{SP3CTR4L_AUD10_CYPH3R}`
    - Tick participant score sheet and award **Prize Token #1** immediately!

---

### Phase 3: Challenge 2 — Video Plate De-Blur (0:55 – 1:55 | 60 mins)
- **Reveal Ch 1 & Demo 2 (0:55 – 1:05 | 10 mins):**
  - Project the reference spectrogram output on screen.
  - Transition to Video Forensics: *"In video surveillance, moving objects experience motion smear due to shutter integration. We cannot de-blur the whole video at once. First, we identify temporal deceleration points — the 'Golden Frames' — and then apply high-pass edge sharpening."*
  - Demonstrate stepping frames in VLC or browsing `frames/` to find where the dark Camry turns or brakes.
- **Hands-On Solving (1:05 – 1:55 | 50 mins):**
  - Participants inspect `surveillance_traffic.mp4` (or `frames/`).
  - **Timed Hint Ladder:**
    - **@ 15 mins (1:20):** *"Do not try to read the plate during high-speed travel. Scan through the frames to locate where the vehicle is closest and decelerating."*
    - **@ 30 mins (1:35):** *"Check frames #80 to #95 (around timestamp 16:24:32). Frame #90 gives you the clearest view of the front bumper."*
    - **@ 40 mins (1:45):** *"Crop the plate in GIMP or Photoshop, and apply 'Unsharp Mask' with radius 2.0 and amount 200–250%, then increase the contrast. The plate starts with 'VB'."*
  - **Verification & Prize:**
    - Flag: `FLAG{PL4T3_VB698108_CLR}` (or `VB 698 108`)
    - Tick participant score sheet and award **Prize Token #2**!

---

### Phase 4: Challenge 3 — Crime Scene Forensic ELA (1:55 – 2:55 | 60 mins)
- **Reveal Ch 2 & Demo 3 (1:55 – 2:05 | 10 mins):**
  - Project the de-blurred license plate solution on screen.
  - Transition to Image ELA: *"JPEG compression saves images in 8x8 pixel blocks. When an image is resaved repeatedly, compression errors stabilize. When a new element (like an evidence weapon) is digitally composited from another source and resaved, it exhibits much higher compression difference than the unedited background."*
  - Demonstrate opening `solutions/offline_ela_viewer.html` or GIMP difference mode, and explain how to ignore natural high-contrast edges (cones A & B) and look for areal compression discrepancies.
- **Hands-On Solving (2:05 – 2:55 | 50 mins):**
  - Participants inspect `crime_scene_evidence.jpg`.
  - **Timed Hint Ladder:**
    - **@ 15 mins (2:20):** *"Do not be deceived by natural high-contrast borders like yellow cones A & B or black censor bars. True digital splicing causes the ENTIRE object to glow with irregular compression error."*
    - **@ 30 mins (2:35):** *"Look closely at the revolver resting near the victim's left hand and its attached evidence tag. Compare its error rate to the floor and blood beneath it."*
    - **@ 40 mins (2:45):** *"The medical examiner noted the victim died of blunt trauma with zero GSR. The gun was digitally staged! The flag format is `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}`."*
  - **Verification & Prize:**
    - Flag: `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}`
    - Award **Prize Token #3** (Grand Prize / Forensic Master Badge)!

---

### Phase 5: Conclusion & Awards (2:55 – 3:00 | 5 mins)
- Reveal all three answers on the big screen.
- Acknowledge fastest solvers and top teams.
- Wrap-up discussion on real-world digital forensics and chain of custody.

---

## 3. Buffer Transition (15 Minutes Between Batches)
1. Clear the physical score sheet and prepare fresh sheets for the next batch.
2. Restock candy, stickers, and prize tokens.
3. Check HTTP server status and verify local IP hasn't changed.
4. Welcome Batch 2 / Batch 3 participants.

---

## 4. Master Flag Key & Troubleshooting
| Challenge | Category | Target Flag | Common Participant Pitfall & Fix |
| :--- | :--- | :--- | :--- |
| **Ch 1 (Easy)** | Audio Spectrogram | `FLAG{SP3CTR4L_AUD10_CYPH3R}` | **Pitfall:** Spectrogram text looks squished.<br>**Fix:** Remind them Audacity defaults to Logarithmic; they must set Scale to **Linear** in Spectrogram Settings. |
| **Ch 2 (Med)** | Video CCTV De-blur | `FLAG{PL4T3_VB698108_CLR}`<br>*(or `VB 698 108`)* | **Pitfall:** Participant tries to read plate on blurred moving frames.<br>**Fix:** Direct them to deceleration Golden Frame **#090** and apply Unsharp Mask (radius 2.0, amount 220%). |
| **Ch 3 (Hard)** | Crime Scene ELA | `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}` | **Pitfall:** Getting distracted by bright edges on yellow cones A & B.<br>**Fix:** Remind them of edge frequency physics: look for high error across the *entire interior area* of an item in GIMP. |
| **Ch 4 (Med)** | Document ELA | `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}` | **Pitfall:** Not seeing the glowing forged clearance block.<br>**Fix:** Advise performing GIMP layer difference with levels amplification (or demonstrating via `solutions/offline_ela_viewer.html`) and zooming into the lower-right box. |
| **Ch 5 (Med)** | Stereo Spectrogram | `FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}` | **Pitfall:** Audio characters appear scrambled and unreadable in mono.<br>**Fix:** Remind them the audio is stereo; they must click track dropdown &rarr; `Split Stereo Track` to inspect Left and Right separately. |
