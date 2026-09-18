# Challenge 4 Walkthrough & Solution Guide

## Challenge Summary
- **Challenge Name:** Operation Rogue Credential
- **Difficulty:** Medium
- **Category:** Document Forensics / Error Level Analysis (ELA)
- **Target File:** `challenges/challenge4_medium_ela/evidence_clearance_badge.jpg`
- **Official Flag:** `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}`

---

## Technical Background: Error Level Analysis on Official Credentials
Error Level Analysis (ELA) identifies differences in JPEG compression error across an image. 
- When a document or badge is originally created and saved as a JPEG, all pixels undergo compression quantization together.
- When an attacker re-opens the JPEG, alters a specific section (e.g., splicing a "Level 4" authorization block over a "Level 1" section) using uncompressed or newly generated graphics, and resaves the composite as a new JPEG, the newly spliced pixels undergo their **first generation** of compression, resulting in significantly higher error rates (represented by bright multi-colored noise) than the surrounding pre-compressed background.
- In `evidence_clearance_badge.jpg`, the ambient badge was compressed at Quality 70, while the forged clearance block was added uncompressed before a master save at Quality 95, creating a massive **16x error level anomaly ratio**.

---

## Step-by-Step Solution

### Method 1: Professional Forensic Analysis in GIMP (Participant Method)
1. Open `evidence_clearance_badge.jpg` in GIMP.
2. Choose `File -> Export As...` and save as `temp_resave.jpg` with **Quality: 90%**.
3. Choose `File -> Open as Layers...` and select `temp_resave.jpg`.
4. Change the upper layer mode to **Difference**.
5. Select `Layer -> New from Visible`.
6. Open `Colors -> Levels` (or `Colors -> Brightness-Contrast`) and slide the white point to the left to amplify differences ~30x.
7. The fraudulent clearance patch illuminates sharply against the dark card baseline.
8. Zoom in to read the glowing text inside the bounding box:
   ```
   FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
   ```

### Method 2: Instructor Web ELA Inspector
1. Open `solutions/offline_ela_viewer.html` or the portal's `ela_tool.html` in a web browser.
2. Load `evidence_clearance_badge.jpg`.
3. Slide **Resave Quality** to `90%` and **Error Amplification** to `30x`.
4. Observe the document:
   - The agency header, operative photo, barcode, and personal text remain dark and uniform.
   - The entire lower-right rectangle `(X: 310 to 875, Y: 350 to 560)` glows intensely with vibrant high-frequency artifacts.

### Method 3: Headless Automated Verification
Run the automated solver:
```bash
python3 solutions/challenge4_medium_ela/solve_ch4_ela.py
```
Output:
```
[*] Running Document ELA Solver on: challenges/challenge4_medium_ela/evidence_clearance_badge.jpg
[+] ELA difference map saved to: solutions/challenge4_medium_ela/recovered_badge_ela.png
[*] Authentic ID / Photo region error: 0.157
[*] Spliced Clearance patch error:    2.553
[+] Compression Anomaly Ratio:        16.21x

[✓] FORENSIC CONFIRMATION: DIGITAL SPLICING EXPOSED ON SECURITY CLEARANCE BLOCK!
[✓] RECOVERED AUTH OVERRIDE TOKEN: FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
```

---

## Facilitator Hint Progression
- **@ 15 mins:** "Look at the overall compression levels of the badge. Does the clearance level block have the same error signature as the agent photo and header?"
- **@ 30 mins:** "Perform ELA in GIMP (or examine the difference layer) and set levels amplification to ~30x. Look for a sharp rectangular boundary where the noise jumps dramatically."
- **@ 40 mins:** "The forged block contains an override token formatted as `FLAG{3L4_...}`. Zoom directly into the glowing red stamp region."
