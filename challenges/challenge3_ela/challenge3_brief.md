# Challenge 3: Case 1 — The Staged Crime Scene (Hard)

## Incident Overview
**Classification:** HOMICIDE INVESTIGATION // CASE FILE #CRIME-2026-CASE1  
**Target File:** `crime_scene_evidence.jpg`  
**Difficulty:** Hard  
**Theme:** Image Forensics & Error Level Analysis (ELA) on Complex Crime Scenes

---

## Case Scenario
On September 18, patrol officers were dispatched to a reported suicide inside a residential room. The initial incident responder submitted an official crime scene photograph (`crime_scene_evidence.jpg`) showing the deceased victim lying on the wooden floor with a pool of blood, two yellow evidence marker cones (**A** and **B**), and a black revolver resting on the blood pool near the victim's left hand.

However, the medical examiner's forensic autopsy report arrived with startling conclusions:
1. The victim died from blunt force trauma to the occipital region of the cranium, NOT a gunshot wound.
2. The victim had **zero gunshot residue (GSR)** on their hands, skin, or clothing.
3. The blood spatter pattern suggests the weapon was placed after the blood had begun to coagulate.

Chief investigators suspect that a corrupt official or the perpetrator **digitally staged** evidence into the crime scene photograph before entering it into the department evidence vault, intending to close the investigation as an open-and-shut suicide.

As the Senior Forensic Image Analyst, you have been brought in to perform **Error Level Analysis (ELA)** on the evidence photograph to determine which physical item was digitally composited/altered and uncover the forensic tracking token.

---

## Mission Objectives
1. Load `crime_scene_evidence.jpg` into **GIMP (GNU Image Manipulation Program)**.
2. Perform **Error Level Analysis (ELA)** across the crime scene by calculating the layer difference against a 90% re-saved reference copy.
3. **Overcome Forensic Red Herrings:** Natural high-contrast edges (like the yellow marker cones A and B, or the black censor bar over the eyes) naturally generate high-frequency compression edges. Distinguish between normal edge frequency response and **true areal compression manipulation**.
4. Identify the staged physical evidence item that exhibits an unnatural compression error rate across its entire surface.
5. Inspect the staged item and retrieve the official forensic evidence token.
6. Submit the flag in the format: `FLAG{...}`

---

## Step-by-Step Forensic Investigation in GIMP

### Step 1: Open Evidence File
- Launch GIMP and open `crime_scene_evidence.jpg` (`File -> Open...`).

### Step 2: Generate Controlled Re-save Layer (Quality = 90%)
- Export a temporary copy: `File -> Export As...`
- Name the file `temp_resave.jpg` and click **Export**.
- In the JPEG Options dialog:
  - Set **Quality:** `90` (uncheck any extra smoothing).
  - Click **Export**.

### Step 3: Align Both Compression States as Layers
- Load the newly created copy directly over the original:
  `File -> Open as Layers... -> temp_resave.jpg`.
- You now have two layers in the Layers panel on the right:
  - Top layer: `temp_resave.jpg` (1-generation resaved)
  - Bottom layer: `crime_scene_evidence.jpg` (original evidence)

### Step 4: Subtract Layers (Difference Blending Mode)
- Select the top layer (`temp_resave.jpg`).
- In the Layers dropdown menu (where it says **Mode: Normal**), change the blending mode to **Difference**.
- *Mathematical principle:* Identical compression pixels subtract to pure black (`0, 0, 0`), while freshly modified pixels produce subtle non-zero residual differences.

### Step 5: Amplify Residual Error Matrix
- Merge the visible difference into an editable layer:
  `Layer -> New from Visible`.
- Boost the microscopic differences into human visual range:
  - Go to `Colors -> Levels...`.
  - Drag the right-hand white slider significantly to the left (e.g. input levels `0` to `25` or `30`), or go to `Colors -> Brightness-Contrast` and boost brightness.
- Zoom in and inspect the scene:
  - The floor, victim, and blood pool remain dark.
  - One specific staged physical item illuminates brightly with multi-colored artifact noise across its entire body!
- Read the evidence token located on the staged item.

---

## Flag Format
```
FLAG{...}
```
*Submit your verified forensic flag to complete Case 1 and clear the investigation!*
