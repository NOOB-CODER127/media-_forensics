# Challenge 3 (Hard): Crime Scene Forensic ELA Walkthrough

## Challenge Summary
- **Challenge Name:** Case 1 — The Staged Crime Scene
- **Difficulty:** Hard
- **Category:** Digital Image Forensics / Error Level Analysis (ELA)
- **Target File:** `crime_scene_evidence.jpg`
- **Source Material:** Real crime scene photograph (`Case-1-dead-body-and-crime-scene-at-the-finding.webp`)
- **Staged Item:** Staged Revolver (.38 Special) & Attached Forensic Tag #01-W
- **Official Flag:** `FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}`

---

## Technical Background: Why This is a Hard Forensic Challenge

### 1. High-Contrast Distractors vs Areal Manipulation
When performing Error Level Analysis on photographic evidence:
- **Sharp Edge Boundaries** (such as the bright yellow evidence marker cones A and B, high-contrast blood edges, or black censor bars) have high spatial frequencies. In lossy JPEG compression, high-frequency DCT coefficients always have higher quantization loss than smooth areas. An inexperienced analyst often mistakes these normal edge frequencies for tampering.
- **Areal Compression Discrepancies:** Genuine digital splicing or compositing from another image source causes the **entire interior surface** of the doctored object to suffer a distinct compression error rate compared to the surrounding environment.

### 2. Forensic Discrimination
In `crime_scene_evidence.jpg`:
- The background room, floorboards, victim clothing, and bed were compressed at an established camera quantization baseline ($Q \approx 75$).
- The weapon and its forensic label were composited at a different quantization state ($Q \approx 95$).
- When re-quantized during ELA at $Q=90$, the floor and clothing experience minimal additional error ($\approx 0.75$), while the entire revolver body and its tag illuminate brightly with an error rate exceeding $2.4$ ($>3.1\times$ contrast ratio).

---

## Step-by-Step Solution

### Step 1: Perform Error Level Analysis in GIMP
1. Open `crime_scene_evidence.jpg` in GIMP (`File -> Open`).
2. Export a reference resave at 90% quality: `File -> Export As... -> temp_resave.jpg` (Quality = 90).
3. Load the resaved image as a new layer: `File -> Open as Layers... -> temp_resave.jpg`.
4. In the Layers panel, switch the mode of `temp_resave.jpg` from **Normal** to **Difference**.
5. Select `Layer -> New from Visible`, then open `Colors -> Levels` and slide the white point to the left to amplify differences ~30x.
*(Alternatively, instructors can demonstrate using `solutions/offline_ela_viewer.html` or automated script `python3 solutions/challenge3_ela/solve_ch3_ela.py`)*.

### Step 2: Analyze the ELA Output
Compare the areas of interest:
1. **Evidence Marker A & B:** While their yellow borders show typical high-contrast edge noise, their flat interior yellow surfaces have low, uniform error matching the wooden floor.
2. **The Victim:** The white t-shirt and tan trousers show consistent, uniform error levels across all fabric folds.
3. **The Revolver & Evidence Tag:** Unlike the rest of the room, the **entire body of the revolver** (from the cylinder and barrel to the grip) and the **attached evidence tag** illuminate brightly with intense, multi-colored high error levels.

See reference solution: [reference_crime_scene_ela.png](file:///home/prab/med-for-cha/solutions/challenge3_ela/reference_crime_scene_ela.png).

### Step 3: Extract the Evidence Token
Zoom in on the illuminated weapon at `X: 250-470, Y: 490-615`:
The forensic evidence tag attached directly beneath the revolver reads:
```
FORENSIC EVIDENCE TAG #01-W
FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}
```

The recovered flag is:
`FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}`

---

## Facilitator Hint Progression
- **10 Minutes:** "Do not be distracted by the bright edges of yellow markers A and B. In ELA, look for an entire object whose body glows differently from the floor."
- **18 Minutes:** "Check the revolver resting on the blood pool near the victim's hand. Compare its internal error density to the surrounding wood grain and blood."
- **25 Minutes:** "Zoom in on the revolver and the white evidence tag attached below it. Read the forensic verification string starting with `FLAG{`."
