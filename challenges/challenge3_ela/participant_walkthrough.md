# Participant Walkthrough: Challenge 3 (Image Forensics & ELA)

## Case: The Staged Crime Scene (Case 1)
- **Difficulty:** Hard
- **Forensic Tool:** GIMP (GNU Image Manipulation Program)
- **Target Evidence:** `crime_scene_evidence.jpg`
- **Objective:** Expose the digitally composited evidence weapon in the crime scene photograph and recover the forensic tag token.

---

### Investigation Overview & Forensic Theory
The victim was discovered deceased on a bedroom floor. An autopsy report indicated death was caused by blunt force trauma with **zero Gunshot Residue (GSR)**, yet an evidence revolver rests directly beside the victim's hand. Investigators suspect the gun was digitally fabricated into the crime scene photograph after the fact.

#### What is Error Level Analysis (ELA)?
JPEG compression divides images into 8x8 pixel blocks and quantizes frequency components. 
- When an image is resaved repeatedly at the same quality level, compression error reaches equilibrium and produces minimal new error upon further resaves.
- If a new object (such as a weapon) is composited into an existing image from an external source with a higher compression quality, that object will undergo an earlier generation of compression.
- When re-compressed at a standardized quality (such as 90%), the unedited background will show very little error (dark), whereas the newly spliced object will show intense compression error (bright, colorful noise).

#### Crucial Forensic Distinction: Edges vs Areal Tampering
- **Natural High-Contrast Edges (Red Herrings):** Sharp color boundaries (such as the bright yellow evidence cones A and B, blood boundaries, or black censor bars) naturally produce high-frequency edge response. Look inside their flat surface—the interior of cones A and B remains dark and uniform.
- **Areal Tampering (Genuine Forgery):** A digitally staged element exhibits high error across its **entire body** (barrel, cylinder, hammer, grip, and attached label).

---

### Step-by-Step Solution in GIMP

#### Step 1: Open the Evidence Image in GIMP
1. Launch **GIMP**.
2. Go to `File -> Open...` and select `crime_scene_evidence.jpg`.

#### Step 2: Export a Reference Resave at 90% Quality
1. Go to `File -> Export As...`.
2. Name the file `temp_resave.jpg` (save it in your working directory).
3. Click **Export**.
4. In the JPEG Export dialog box:
   - Ensure the **Quality slider is set to 90%**.
   - Click **Export**.

#### Step 3: Load the Reference Copy as a Layer
1. In GIMP, go to `File -> Open as Layers...`.
2. Select the `temp_resave.jpg` you just created.
3. You now have two layers in your **Layers dock** (`Ctrl + L`):
   - Top layer: `temp_resave.jpg`
   - Bottom layer: `crime_scene_evidence.jpg`

#### Step 4: Compute the Difference Map
1. In the **Layers** panel on the right, click to select the top layer (`temp_resave.jpg`).
2. Click the **Mode** dropdown menu (which currently says *Normal*).
3. Scroll through the blend modes and select **Difference**.
4. The canvas will turn almost completely black. This is expected—the difference between a 95% and 90% JPEG is only a few pixel intensity values and must be amplified.

#### Step 5: Amplify the Compression Differences
1. Go to `Layer -> New from Visible` (this creates a single flattened layer representing the difference map).
2. Ensure this new visible layer is selected.
3. Open `Colors -> Levels...`:
   - Under **Input Levels**, locate the rightmost white triangle slider (set at 255).
   - Drag this white slider to the left toward **15 – 25**.
   *(Alternatively, use `Colors -> Brightness-Contrast...` and boost brightness and contrast to near maximum)*.
4. Click **OK**.

#### Step 6: Analyze the Illuminated Forensic Anomalies
Inspect the amplified difference canvas:
1. **Evidence Markers A & B:** Note that only their outer silhouette outlines show thin white lines (natural edge frequency). Their flat yellow bodies remain dark, matching the wooden floor.
2. **Victim's Body & Bedding:** Exhibit uniform, low-level error across fabric folds.
3. **The Staged Revolver:** Near the victim's left hand on the blood pool (`X: 250–470, Y: 490–615`), an entire object glows intensely with multi-colored, high-amplitude error across its cylinder, barrel, grip, and attached rectangular tag! This confirms it was digitally inserted.

#### Step 7: Read the Evidence Tag Token
1. Zoom in closely on the glowing white tag attached directly beneath the revolver's cylinder.
2. Read the embossed evidence verification string:
```
FORENSIC EVIDENCE TAG #01-W
FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}
```

#### Step 8: Flag Verification
Submit the extracted token:
```
FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}
```
Verify the flag in the Lab Portal to solve the case!
