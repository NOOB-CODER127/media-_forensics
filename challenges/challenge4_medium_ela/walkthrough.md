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

#### Step 6: Identify the Forged Clearance Block
Examine the amplified difference output across the badge:
1. **Authentic Fields:** The operative photo, barcode, security chip, operative details (`OP_VANCE_90421`), facility sector (`SEC4_EXT_0994`), and expiration date (`AUD_PASS_2028`) remain completely dark and uniform (error rate ~0.15).
2. **Forged Spliced Block:** The entire lower-right clearance classification block (`X: 310 to 885, Y: 335 to 555`) illuminates with sharp brightness and multi-colored compression noise (error rate ~0.92, a **6x anomaly ratio**).
3. The crisp rectangular border clearly delineates where the digital Level 4 block was composited over the original Level 1 section.

#### Step 7: Read the Fraudulent Clearance Token & Flag
1. Zoom in on the glowing clearance block (`X: 310 to 885, Y: 335 to 555`).
2. Read the token associated with the spliced credential:
```
SECURITY CLEARANCE TOKEN: CL34R4NC3_0V3RR1D3
```
3. Format the official flag:
```
FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
```

#### Step 8: Flag Verification
Submit the verified token in the Lab Portal:
```
FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
```
*(The portal also accepts `CL34R4NC3_0V3RR1D3` or `0V3RR1D3`)*. Validation confirms the clearance fraud!
