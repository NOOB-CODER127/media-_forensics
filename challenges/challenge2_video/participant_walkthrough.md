# Participant Walkthrough: Challenge 2 (Video Forensics)

## Case: Operation Ghost Vehicle
- **Difficulty:** Medium
- **Forensic Tools:** VLC Media Player (or any frame-stepping video player) & GIMP
- **Target Evidence:** `surveillance_traffic.mp4` (and pre-extracted `frames/` directory)
- **Objective:** Identify the suspect sedan, pinpoint the optimal focal frame, enhance the motion-blurred license plate, and recover the registration number.

---

### Investigation Overview & Theory
CCTV traffic cameras capture vehicles moving at varying velocities and angles relative to the camera sensor. 
- When a car is far away, the plate covers only a few dozen pixels and cannot be resolved.
- When a car accelerates or turns sharply across the sensor's field of view, horizontal motion blur obscures character strokes.
- **The Deceleration Apex:** As a vehicle approaches an intersection or stops in traffic, there is a momentary window where velocity drops and the vehicle is at its closest distance to the optical lens. This frame provides maximum pixel density with minimal motion blur.

---

### Step-by-Step Solution

#### Step 1: Video Review & Frame Scrubbing
1. Open `surveillance_traffic.mp4` in **VLC Media Player**.
2. Identify the vehicle of interest: a dark metallic **Toyota Camry sedan** traveling toward the camera down the center lane.
3. Review the timeline:
   - **0.0s – 2.5s (Frames #001 to #060):** Vehicle is too far up the street. The plate is under 20 pixels wide and illegible.
   - **3.1s – 4.0s (Frames #075 to #095):** The car slows down significantly as it reaches the foreground directly facing the camera sensor.
   - **3.75s (Frame #090, OSD timestamp 16:24:32):** The vehicle reaches the **Deceleration Apex**—the exact instant where the front bumper is closest to the lens before the car banks out of the focal zone.

#### Step 2: Open the Golden Frame in GIMP
1. If using the provided `frames/` folder, locate and open `frames/frame_090.png` in **GIMP**.
   *(If extracting from video manually in VLC: pause around 3.7s and use `Video -> Take Snapshot`, or use FFmpeg: `ffmpeg -ss 00:00:03.750 -i surveillance_traffic.mp4 -vframes 1 apex.png`)*.
2. In GIMP, zoom in on the front bumper area (`Ctrl + Mouse Wheel`).

#### Step 3: Crop the License Plate
1. Select the **Rectangle Select Tool** (`R`).
2. Draw a tight bounding box around the front license plate mounted on the lower center bumper (`X: ~550 to 675, Y: ~390 to 445`).
3. Select `Image -> Crop to Selection`.
4. Observe that the white rectangular plate contains stamped characters softened by slight forward motion and atmospheric glare.

#### Step 4: Apply Forensic Unsharp Masking
To bring out the crisp character edges from the motion blur:
1. Go to `Filters -> Enhance -> Unsharp Mask...`.
2. Configure the filter settings:
   - **Radius:** `2.0`
   - **Amount (Strength):** `2.2` (or `220%`)
   - **Threshold:** `2`
3. Click **OK**.
4. The high-contrast edges of the embossed characters will immediately sharpen against the plate background.

#### Step 5: Boost Contrast
1. Go to `Colors -> Brightness-Contrast...`.
2. Increase **Contrast** (slide right, around `+40` to `+60`) and slightly lower **Brightness** if needed.
3. This suppresses noise on the reflective white backing and pushes the dark stamped characters toward solid black.

#### Step 6: Decipher the Registration Plate
Examine the sharpened characters on the plate:
```
+------------------------------------+
|            VB 698 108              |
+------------------------------------+
```
- First two characters: `VB`
- Middle group: `698`
- Last group: `108`

#### Step 7: Flag Verification
Submit the plate code in standard flag format or raw string:
```
FLAG{PL4T3_VB698108_CLR}
```
*(Alternative accepted format in portal: `VB 698 108`)*.
