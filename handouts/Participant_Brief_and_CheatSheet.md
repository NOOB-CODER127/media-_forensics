# Media Forensics & Deepfake Lab — Participant Cheat Sheet

> **Theme:** *"You are the digital forensic analyst – uncover the truth hidden in pixels, frames, and sound."*

---

## Lab Schedule (3-Hour Session)
| Timeline | Phase | What You Do |
| :--- | :--- | :--- |
| **0:00 – 0:15** | Setup & Briefing | Connect to Zone Wi-Fi, download challenge archives from Local Portal |
| **0:15 – 0:25** | Challenge 1 Demo | Live demonstration of Audio Spectrogram Steganography principles |
| **0:25 – 0:55** | **Challenge 1 (Easy)** | **Solve Operation Whispering Wiretap (Audio Spectrogram - 30 mins)** |
| **0:55 – 1:05** | Answer & Demo 2 | Reveal Challenge 1, live demo of Video Frame Extraction & Sharpening |
| **1:05 – 1:55** | **Challenge 2 (Medium)** | **Solve Operation Ghost Vehicle (Video CCTV Plate - 50 mins)** |
| **1:55 – 2:05** | Answer & Demo 3 | Reveal Challenge 2, live demo of Error Level Analysis (ELA) on crime scenes |
| **2:05 – 2:55** | **Challenge 3 (Hard)** | **Solve Case 1: The Staged Crime Scene (Crime Scene ELA - 50 mins)** |
| **2:55 – 3:00** | Conclusion & Awards | Final flag verification, wrap-up Q&A, prize token distribution |

---

## 1. Audio Forensics & Spectrogram Cheat Sheet (Challenge 1)

### Working with Audacity
1. **Open File:** `File -> Open... -> intercepted_wiretap.wav`
2. **Switch to Spectrogram:**
   - Click the track dropdown chevron `▼` (next to `intercepted_wiretap` on the left track panel).
   - Select **Spectrogram**.
3. **Calibrate Spectrogram for Text Steganography:**
   - Click dropdown `▼` again -> **Spectrogram Settings...**
   - **Scale:** Change from `Logarithmic` to **`Linear`** *(Crucial!)*
   - **Window size:** `1024` or `2048`
   - **Max Frequency:** `16000 Hz`
   - **Min Frequency:** `7000 Hz`
   - Click **Apply**.
4. **Zooming:**
   - Use `Ctrl + 1` (Zoom in) or hold `Ctrl` and scroll mouse wheel to inspect the timeline between **2.5s and 14.5s**.

---

## 2. Video Forensics & Frame Extraction Cheat Sheet (Challenge 2)

### Target Vehicle:
Dark metallic Toyota Camry sedan driving along wet asphalt.

### Common FFmpeg Commands
```bash
# 1. Extract all video frames as PNGs (lossless)
ffmpeg -i surveillance_traffic.mp4 -vsync 0 frames/frame_%03d.png

# 2. Extract frames from the Golden Apex deceleration window (3.5s - 4.0s)
ffmpeg -ss 00:00:03.500 -i surveillance_traffic.mp4 -t 00:00:00.800 frames/apex_%02d.png
```

### Frame Stepping in VLC
- Press the `E` key in VLC media player to step through video playback frame-by-frame.
- Take a snapshot of candidate deceleration frames using `Shift + S`.

### Image Sharpening in Photo Editors (GIMP / Photoshop)
- Inspect candidate frame (e.g. `frame_090.png`).
- Crop the front bumper license plate.
- **Unsharp Mask:** `Filters -> Enhance -> Sharpen (Unsharp Mask...)`
  - Try Radius `2.0` and Amount `200% - 250%`.
- **Contrast:** `Colors -> Brightness-Contrast` to boost contrast by 1.5x–2.0x to separate dark stamped characters from reflective plate glare.

---

## 3. Crime Scene Image Forensics & ELA Cheat Sheet (Challenge 3)

### What is Error Level Analysis (ELA)?
When an image is modified and re-saved as a JPEG, newly inserted/modified elements exhibit a distinct compression error rate compared to original unedited regions.

### Avoiding Red Herrings:
- **Natural High-Contrast Edges:** High contrast borders (like yellow evidence markers or black censor blocks) naturally show high-frequency edge response. Look inside the object surface.
- **Areal Tampering:** Digitally staged objects (like a composite weapon) glow brightly across their entire body (cylinder, barrel, grip, tag) compared to the surrounding floor.

### Recommended Forensic Tool: GIMP (GNU Image Manipulation Program)
Perform professional 5-step manual Error Level Analysis:
1. **Open Image:** `File -> Open -> crime_scene_evidence.jpg`.
2. **Export Reference at 90% Quality:** `File -> Export As... -> temp_resave.jpg`. In the JPEG export dialog, ensure Quality is set to **90%** and click **Export**.
3. **Load Reference as Layer:** `File -> Open as Layers... -> temp_resave.jpg`.
4. **Compute Difference:** In the **Layers** dockable dialog, change the top layer **Mode** from `Normal` to **Difference**.
5. **Amplify Artifacts:** Select `Layer -> New from Visible`, then open `Colors -> Levels` (or `Colors -> Brightness-Contrast`). Drag the white input point to the left to amplify subtle compression differences.

---

## 4. Document Forensics & Badge ELA Cheat Sheet (Challenge 4)

### Background:
Official credentials and ID badges should exhibit consistent compression history across all printed fields. When an unauthorized access level (e.g. Level 4) is digitally spliced onto a baseline badge, the spliced rectangle exhibits an enormous compression anomaly compared to the authentic photo and agency headers.

### Detection Workflow in GIMP:
1. **Open Image:** Load `evidence_clearance_badge.jpg` in GIMP (`File -> Open`).
2. **Export Reference:** Export a reference copy as `temp_badge_resave.jpg` at **90% Quality**.
3. **Open as Layer:** Go to `File -> Open as Layers...` and select `temp_badge_resave.jpg`.
4. **Set Mode to Difference:** Change the layer blend mode to **Difference**.
5. **Amplify Error Levels:** Go to `Layer -> New from Visible`, then open `Colors -> Levels` and slide the white slider left (or increase contrast/brightness ~25x).
6. **Identify Splice:** Look for the brightly glowing rectangular boundary over the clearance block and read the digital clearance override token.

---

## 5. Stereo Audio Spatial Spectrogram Cheat Sheet (Challenge 5)

### Working with Multi-Channel Audio in Audacity:
1. **Open File:** `File -> Open... -> covert_broadcast.wav` (Stereo).
2. **Decouple Channels:** Click track dropdown chevron `▼` &rarr; choose **Split Stereo Track**.
3. **Spectrogram Setup:**
   - On Track 1 (Left Channel): Select **Spectrogram**, set Scale to **Linear**, frequency band **5,000 Hz – 14,000 Hz**.
   - On Track 2 (Right Channel): Select **Spectrogram**, set Scale to **Linear**, frequency band **5,000 Hz – 14,000 Hz**.
4. **Read & Concatenate:**
   - Read Part 1 from the Left channel: `FLAG{DU4L_...`
   - Read Part 2 from the Right channel: `..._SP3CTRUM}`
   - Join both parts into a single string.

---

## Flag Submission Format
All flags follow the standard format:
- Challenge 1: `FLAG{SP3CTR4L_AUD10_CYPH3R}`
- Challenge 2: `FLAG{PL4T3_VB698108_CLR}` *(or `VB 698 108`)*
- Challenge 3: `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}`
- Challenge 4: `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}`
- Challenge 5: `FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}`

*Submit each flag on the Local Lab Portal or directly to your Zone Lead for validation and prize tokens!*
