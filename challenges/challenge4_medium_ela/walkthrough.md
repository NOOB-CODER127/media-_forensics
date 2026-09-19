# Participant Walkthrough: Challenge 4 (Document Forensics & Badge ELA)

## Case: Operation Rogue Credential
- **Difficulty:** Medium
- **Forensic Tool:** GIMP (GNU Image Manipulation Program)
- **Target Evidence:** `evidence_clearance_badge.jpg`
- **Objective:** Detect the digitally forged security clearance splice on the credential badge and recover the unredacted authorization override code.

---

### Investigation Overview & Forensic Theory
A contractor's electronic keycard was used to gain unauthorized entry into a Level-4 physical security vault. Visually, the contractor's laminated badge clearly says **LEVEL 4 - TOP SECRET**. However, access control logs show this operative was only ever issued a **Level 1** clearance.

#### Document Forensics with Error Level Analysis
When an authentic credential document or badge is generated and saved as a JPEG, all visual elements (agency emblem, photo, barcode, and text fields) undergo the same compression cycle simultaneously.
- If a bad actor tampers with the credential by pasting a new "Level 4" authorization block from an uncompressed graphic or another document and resaves the image, that altered rectangular area will undergo its **first generation of compression**, while the authentic portion of the badge is on its **second (or later) generation**.
- Under Error Level Analysis (ELA), the authentic card body reaches a low error state, while the spliced rectangle illuminates brilliantly with high error noise (up to **16x higher** than the baseline badge).

---

### Step-by-Step Solution in GIMP

#### Step 1: Open the Badge Evidence
1. Launch **GIMP**.
2. Go to `File -> Open...` and select `evidence_clearance_badge.jpg`.
3. Visually examine the badge: the typography, background patterning, photo, and barcode all appear consistent to the naked eye.

#### Step 2: Export a Reference Resave at 90% Quality
1. Go to `File -> Export As...`.
2. Name the file `temp_badge_resave.jpg`.
3. Click **Export**.
4. In the JPEG Export dialog:
   - Ensure the **Quality slider is set to 90%**.
   - Click **Export**.

#### Step 3: Open Reference as a Top Layer
1. In GIMP, go to `File -> Open as Layers...`.
2. Select `temp_badge_resave.jpg`.
3. In your **Layers** panel (`Ctrl + L`), confirm you have:
   - Top layer: `temp_badge_resave.jpg`
   - Bottom layer: `evidence_clearance_badge.jpg`

#### Step 4: Apply Difference Blend Mode
1. Select the top layer (`temp_badge_resave.jpg`).
2. Click the **Mode** dropdown menu (default is *Normal*).
3. Select **Difference**.
4. The canvas will turn black with faint, barely visible pixels.

#### Step 5: Amplify the Error Differences
1. Go to `Layer -> New from Visible` (creates a combined difference layer).
2. Go to `Colors -> Levels...`:
   - Under **Input Levels**, drag the rightmost white triangle slider to the left toward **20 – 30**.
   *(Alternatively, go to `Colors -> Brightness-Contrast...` and increase both Brightness and Contrast by ~30x)*.
3. Click **OK**.

#### Step 6: Identify the Forged Clearance Rectangle
Examine the amplified difference output across the badge:
1. The Department emblem, operative photo, barcode, and personal text fields remain dark and uniform (error rate ~0.15).
2. The entire lower-right authorization block (`X: 310 to 875, Y: 350 to 560`) illuminates with extreme brightness and intense multi-colored noise (error rate ~2.55, a **16x anomaly**).
3. The crisp rectangular border clearly delineates where the digital crop was spliced over the original Level 1 field.

#### Step 7: Read the Override Token
1. Zoom in on the glowing red/white authorization box in the lower-right quadrant.
2. Read the digital clearance override string:
```
FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
```

#### Step 8: Flag Verification
Submit the extracted token:
```
FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
```
Validate the token in the Lab Portal to confirm the clearance fraud!
