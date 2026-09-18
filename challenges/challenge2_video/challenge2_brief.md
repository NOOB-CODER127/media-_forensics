# Challenge 2: Operation Ghost Vehicle (Medium)

## Incident Overview
**Classification:** TRAFFIC SURVEILLANCE INVESTIGATION // CASE FILE #METRO-2026-042  
**Target Video:** `surveillance_traffic.mp4` (or `gemini_generated_video_e98116b6.mp4` / `frames/`)  
**Difficulty:** Medium  
**Theme:** Video Forensics, Frame Extraction & Plate De-Blurring

---

## Case Scenario
On September 17, 2026 at 16:24 UTC, traffic surveillance camera CAM-04 recorded a dark metallic Toyota Camry sedan speeding along a rain-slicked roadway. The vehicle is suspected of involvement in a hit-and-run incident near the perimeter.

Due to vehicle motion, wet asphalt reflections, and camera shutter integration, the vehicle's front license plate is softened and motion-blurred during playback.

As the digital forensic video analyst, your mission is to inspect the surveillance video, isolate the clearest deceleration / focal window, and apply image enhancement filters to de-blur the front license plate.

---

## Mission Objectives
1. Inspect `surveillance_traffic.mp4` (or browse the extracted `frames/` sequence).
2. Locate the **"Golden Window"** (Frames #80 to #95, around timestamp `16:24:32`) where the vehicle approaches closest to the camera sensor.
3. Extract or crop the front bumper license plate from candidate frame(s) (such as **Frame #90**).
4. Apply forensic de-blurring filters:
   - **Unsharp Masking** (Radius: 2.0, Amount: 200–250%, Threshold: 2)
   - **Contrast Adjustment** (Increase contrast by 1.5x–2.0x)
5. Decipher the license plate characters (`VB 698 108`).
6. Submit the flag in the format: `FLAG{PL4T3_VB698108_CLR}` (or the plate string `VB 698 108`).

---

## Recommended Investigative Tools & Methods

### Method 1: Using the Pre-Extracted Frames Folder
- If you don't have FFmpeg installed, simply open the included `frames/` folder.
- Browse to `frame_090.png`.
- Open the image in GIMP, Photoshop, or your favorite photo editor.
- Crop the front bumper plate and apply:
  `Filters -> Enhance -> Sharpen (Unsharp Mask...)` with **Radius: 2.0** and **Amount: 200% - 250%**.
- Boost contrast using `Colors -> Brightness-Contrast`.

### Method 2: Command-Line Frame Extraction with FFmpeg
```bash
# Extract frames around the 3-4 second mark
ffmpeg -ss 00:00:03.500 -i surveillance_traffic.mp4 -t 00:00:01.000 frames/apex_%03d.png
```

---

## Flag Format
```
FLAG{PL4T3_VB698108_CLR}
```
*(Alternative submissions such as `VB 698 108` or `VB698108` are also accepted)*.
