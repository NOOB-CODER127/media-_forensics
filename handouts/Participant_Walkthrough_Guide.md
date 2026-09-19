# Media Forensics & Deepfake Lab — Participant Walkthrough Guide

> **Attendee Reference Manual**  
> This guide provides step-by-step forensic procedures for solving all 5 challenges using standard forensic tools (**Audacity**, **VLC**, and **GIMP**). Refer to these instructions if you encounter difficulties during your investigation.

---

## Table of Contents
1. [Challenge 1 (Easy): Operation Whispering Wiretap (Audio Forensics)](#challenge-1-easy-operation-whispering-wiretap)
2. [Challenge 2 (Medium): Operation Ghost Vehicle (Video CCTV Forensics)](#challenge-2-medium-operation-ghost-vehicle)
3. [Challenge 3 (Hard): Case 1 — The Staged Crime Scene (Image ELA)](#challenge-3-hard-case-1--the-staged-crime-scene)
4. [Challenge 4 (Medium): Operation Rogue Credential (Document ELA)](#challenge-4-medium-operation-rogue-credential)
5. [Challenge 5 (Medium): Operation Blackout Broadcast (Stereo Audio Forensics)](#challenge-5-medium-operation-blackout-broadcast)

---

## Challenge 1 (Easy): Operation Whispering Wiretap
- **Target File:** `intercepted_wiretap.wav`
- **Primary Tool:** Audacity
- **Core Concept:** High-Frequency Audio Spectrogram Steganography

### Forensic Investigation Steps:
1. **Import File:** Open Audacity and load `intercepted_wiretap.wav` via `File -> Open...`.
2. **Switch to Spectrogram:** Click the downward chevron `▼` next to the track name (`intercepted_wiretap`) on the left track panel and select **Spectrogram**.
3. **Calibrate Settings (Linear Scale):**
   - Click the track chevron `▼` again and choose **Spectrogram Settings...**.
   - Change **Scale** from `Logarithmic` to **`Linear`** *(Crucial: prevents high frequencies from compressing at the top)*.
   - Set **Max Frequency** to `16000 Hz` and **Min Frequency** to `7000 Hz`.
   - Set **Window size** to `1024` or `2048`. Click **OK**.
4. **Zoom & Inspect:** Zoom in (`Ctrl + 1` or `Ctrl + Mouse Wheel`) on the timeline between **2.5s and 14.5s**.
5. **Decipher Message:** Read the illuminated characters in the 9 kHz–14.5 kHz band:
   ```
   FLAG{SP3CTR4L_AUD10_CYPH3R}
   ```

---

## Challenge 2 (Medium): Operation Ghost Vehicle
- **Target File:** `surveillance_traffic.mp4` (and `frames/` folder)
- **Primary Tools:** VLC Media Player & GIMP
- **Core Concept:** CCTV Deceleration Apex Identification & License Plate Unsharp Mask De-blurring

### Forensic Investigation Steps:
1. **Identify the Vehicle:** Play `surveillance_traffic.mp4` in VLC. Identify the dark metallic Toyota Camry sedan driving down the center lane toward the camera.
2. **Locate the Deceleration Apex (Frame #090):**
   - Between 0.0s and 2.5s, the car is distant and resolution is too low.
   - At **3.75 seconds (Frame #090, OSD 16:24:32)**, the car reaches its closest focal distance with minimal motion blur before angling away.
3. **Open Frame #090 in GIMP:** Open `frames/frame_090.png` in GIMP.
4. **Crop the Plate:** Use the Rectangle Select Tool (`R`) to crop the front bumper plate (`X: 550 to 675, Y: 390 to 445`), then choose `Image -> Crop to Selection`.
5. **Apply Unsharp Mask:**
   - Go to `Filters -> Enhance -> Unsharp Mask...`.
   - Set **Radius:** `2.0`, **Amount:** `2.2` (220%), **Threshold:** `2`.
   - Click **OK** to restore high-frequency stamped edges.
6. **Enhance Contrast:** Go to `Colors -> Brightness-Contrast...`, increase Contrast (+40 to +60) to suppress white glare and make characters dark.
7. **Read Plate String:**
   ```
   VB 698 108
   ```
   Flag: `FLAG{PL4T3_VB698108_CLR}` *(or `VB 698 108`)*.

---

## Challenge 3 (Hard): Case 1 — The Staged Crime Scene
- **Target File:** `crime_scene_evidence.jpg`
- **Primary Tool:** GIMP
- **Core Concept:** Error Level Analysis (ELA) — Distinguishing Natural Edge Frequency from Areal Tampering

### Forensic Investigation Steps:
1. **Open Image in GIMP:** Launch GIMP and open `crime_scene_evidence.jpg`.
2. **Export Reference Copy at 90%:**
   - Go to `File -> Export As...` -> name as `temp_resave.jpg`.
   - Set JPEG **Quality to 90%** in the dialog and export.
3. **Load Reference as Layer:** Go to `File -> Open as Layers...` and select `temp_resave.jpg`.
4. **Compute Difference Mode:**
   - In the **Layers** panel (`Ctrl + L`), select the top layer (`temp_resave.jpg`).
   - Change the layer **Mode** dropdown from *Normal* to **Difference**.
5. **Amplify the Compression Error:**
   - Go to `Layer -> New from Visible`.
   - Go to `Colors -> Levels...`. Drag the white input slider from 255 down to **15 – 25** (or use `Colors -> Brightness-Contrast` and maximize contrast).
6. **Forensic Analysis:**
   - Notice yellow markers A & B only have thin edge outlines, while their interior bodies are dark (natural high-frequency edges).
   - Near the victim's hand (`X: 250–470, Y: 490–615`), the **entire body of the revolver and its attached evidence tag** glow brightly with intense multi-colored noise, proving it was digitally inserted.
7. **Read Evidence Tag:** Zoom into the glowing white tag attached below the cylinder:
   ```
   FORENSIC EVIDENCE TAG #01-W
   FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}
   ```

---

## Challenge 4 (Medium): Operation Rogue Credential
- **Target File:** `evidence_clearance_badge.jpg`
- **Primary Tool:** GIMP
- **Core Concept:** Document Integrity Forensics & Compression Generation Differentials

### Forensic Investigation Steps:
1. **Open Badge in GIMP:** Open `evidence_clearance_badge.jpg`. Visually, the badge appears authentic and approved for Level 4.
2. **Export Reference Copy at 90%:** Go to `File -> Export As...` -> save as `temp_badge_resave.jpg` with **Quality = 90%**.
3. **Open as Layer:** Go to `File -> Open as Layers...` -> select `temp_badge_resave.jpg`.
4. **Set Mode to Difference:** Change the top layer Mode to **Difference**.
5. **Amplify Artifacts:**
   - Choose `Layer -> New from Visible`.
   - Open `Colors -> Levels...` and drag the white input slider to **20 – 30**.
6. **Locate the Forgery:**
   - The photo, barcode, and header text stay dark and uniform.
   - The entire lower-right authorization block (`X: 310 to 875, Y: 350 to 560`) illuminates intensely with a **16x error differential**, revealing the spliced rectangular crop boundary.
7. **Read Override Token:** Zoom into the glowing authorization box:
   ```
   FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
   ```

---

## Challenge 5 (Medium): Operation Blackout Broadcast
- **Target File:** `covert_broadcast.wav` (Stereo)
- **Primary Tool:** Audacity
- **Core Concept:** Stereo Spatial Channel Decoupling & Independent Spectral Steganography

### Forensic Investigation Steps:
1. **Open File in Audacity:** Open `covert_broadcast.wav`. Note the track header specifies **Stereo**.
   *(If viewed as combined stereo, both channels print over each other in the same frequency band, creating an illegible jumble)*.
2. **Decouple Stereo Channels:**
   - Click the track chevron `▼` on the left header panel next to `covert_broadcast`.
   - Select **Split Stereo Track**.
   - Audacity decouples the audio into two separate tracks: Track 1 (Left Channel) and Track 2 (Right Channel).
3. **Calibrate Spectrogram on Both Channels:**
   - On **Track 1 (Left Channel)**: Click `▼` -> `Spectrogram`. Click `▼` again -> `Spectrogram Settings...` -> set Scale to **Linear**, Min Frequency **5000 Hz**, Max Frequency **14000 Hz**.
   - On **Track 2 (Right Channel)**: Click `▼` -> `Spectrogram`. Click `▼` again -> `Spectrogram Settings...` -> set Scale to **Linear**, Min Frequency **5000 Hz**, Max Frequency **14000 Hz**.
4. **Read Channel Payloads (Timeline 2.5s – 15.5s):**
   - **Track 1 (Left Channel):** Displays Part 1: `FLAG{DU4L_CH4NN3L_`
   - **Track 2 (Right Channel):** Displays Part 2: `ST3R30_SP3CTRUM}`
5. **Concatenate Passkey:** Join both parts together:
   ```
   FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}
   ```

---

## Quick Reference Summary Table

| Challenge | Category | Primary Tool | Key Technique | Target Flag |
| :--- | :--- | :--- | :--- | :--- |
| **Ch 1 (Easy)** | Audio Forensics | Audacity | Linear Spectrogram (7kHz–16kHz) | `FLAG{SP3CTR4L_AUD10_CYPH3R}` |
| **Ch 2 (Med)** | Video Forensics | VLC + GIMP | Frame #090 Apex + Unsharp Mask (2.0/220%) | `FLAG{PL4T3_VB698108_CLR}` |
| **Ch 3 (Hard)** | Crime Scene ELA | GIMP | 90% Quality Resave Difference + Levels | `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}` |
| **Ch 4 (Med)** | Document ELA | GIMP | 90% Quality Resave Difference + Levels | `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}` |
| **Ch 5 (Med)** | Stereo Audio | Audacity | Split Stereo Track + Linear Spectrogram | `FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}` |
