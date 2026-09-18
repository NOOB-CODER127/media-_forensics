# Challenge 2 (Medium): Video Forensics & License Plate De-blur Walkthrough

## Challenge Summary
- **Challenge Name:** Operation Ghost Vehicle
- **Difficulty:** Medium
- **Category:** Video Forensics / Frame Selection & License Plate De-blur
- **Target Video:** `surveillance_traffic.mp4` / `gemini_generated_video_e98116b6.mp4`
- **Identified Vehicle:** Dark Metallic Toyota Camry Sedan
- **Identified License Plate:** `VB 698 108`
- **Official Flag:** `FLAG{PL4T3_VB698108_CLR}`

---

## Step-by-Step Forensic Solution

### Step 1: Video Review & Frame Selection
Watch the 10-second 24fps surveillance video (`surveillance_traffic.mp4`):
- **Frames 1–60 (0.0s – 2.5s):** The vehicle is distant at the top of the street. The plate is under 25 pixels wide and cannot be reconstructed.
- **Frames 75–95 (3.1s – 4.0s):** The vehicle approaches directly down the center lane toward the camera sensor.
- **Frame #90 (at 3.75s, OSD 16:24:32):** The vehicle is at the optimal focal distance where the front bumper license plate is largest and clearest before passing out of frame.

### Step 2: Crop the Front Plate
In `frame_090.png`, crop the front bumper area:
- Coordinates: `X: 550 to 675, Y: 390 to 445`
- The plate appears as a white rectangular plate with characters softened by horizontal shutter motion.

### Step 3: Apply Forensic Sharpening
Open the crop in GIMP or execute `solution/solve_ch2.py`:
1. **Unsharp Mask:**
   - Radius: `2.0`
   - Amount: `220%` (2.2)
   - Threshold: `2`
   This enhances the high-frequency edge gradients of the stamped alphanumeric characters.
2. **Contrast Enhancement:**
   - Boost contrast by `1.8x` to push the dark characters toward black against the reflective white backing.

### Step 4: Decipher the License Plate
The de-blurred plate reads:
```
+----------------+
|  VB 698 108    |
+----------------+
```

Recovered Flag:
`FLAG{PL4T3_VB698108_CLR}`

---

## Facilitator Hint Progression
- **15 Minutes:** "Don't try to read the plate when the car is far away at the top of the street. Inspect the video between seconds 3.0 and 4.0 (frames #80 to #95)."
- **30 Minutes:** "Open `frame_090.png` from the `frames/` folder. The Toyota Camry is closest to the camera right here."
- **40 Minutes:** "Crop the front bumper plate from `frame_090.png` into an image editor and apply an 'Unsharp Mask' filter with radius 2.0 and amount ~220%, then increase the contrast."
