# Challenge 4: Operation Rogue Credential (Medium)

## Incident Overview
**Classification:** INTERNAL SECURITY BREACH // CASE FILE #SEC-2026-089  
**Target File:** `evidence_clearance_badge.jpg`  
**Difficulty:** Medium  
**Theme:** Document Forensics & Error Level Analysis (ELA)

---

## Case Scenario
At 02:15 AM, security personnel at the High-Security Biometrics & Research Vault detained an individual attempting to enter the Special Access Program facility. The individual presented a laminated departmental security clearance badge (`evidence_clearance_badge.jpg`). 

Visually, the badge appears to be a legitimate credential formatted with official corporate styling, displaying multiple authentication tokens across all sections (Operative Token, Assigned Sector Code, Expiration Audit Token, Hardware Chip UID, and Clearance Token).

However, a query to the central personnel database indicates the contractor was only ever granted **LEVEL 1 (RESTRICTED VISITOR)** privileges. Physical security suspects the badge image was digitally forged by splicing a Level 4 credential block into the official layout prior to lamination.

As the forensic image analyst, your task is to perform **Error Level Analysis (ELA)** on the badge photograph to expose the digital forgery, identify which of the credential fields was spliced, and retrieve the rogue clearance token.

---

## Mission Objectives
1. Load `evidence_clearance_badge.jpg` into **GIMP (GNU Image Manipulation Program)**.
2. Perform **Error Level Analysis (ELA)** across the badge by calculating layer difference against a 90% re-saved reference copy.
3. Compare the compression error rate of the personal details, photograph, and barcode against the clearance section.
4. Confirm digital tampering and locate the forged authorization block.
5. Recover the digital crypto-override token embedded inside the forged region.
6. Submit the flag in the format: `FLAG{...}`

---

## Step-by-Step Forensic Investigation in GIMP

### Step 1: Open Badge Evidence
- Launch GIMP and open `evidence_clearance_badge.jpg` (`File -> Open...`).

### Step 2: Export Controlled Re-save Copy (Quality = 90%)
- Choose `File -> Export As...`
- Name the file `badge_resave.jpg` and click **Export**.
- Set **Quality: 90** and click **Export**.

### Step 3: Layer Alignment
- Load the resaved image as the top layer:
  `File -> Open as Layers... -> badge_resave.jpg`.

### Step 4: Layer Subtraction (Difference Blending Mode)
- In the Layers dock on the right, change the top layer Mode from `Normal` to **`Difference`**.

### Step 5: Contrast & Level Amplification
- Create a combined analysis layer: `Layer -> New from Visible`.
- Inspect the badge:
  - The photo, barcode, agency banner, operative details, and expiration fields remain dark.
  - The lower-right clearance section illuminates with sharp, multi-colored artifact noise (~6x compression error differential)!
- Identify the spliced clearance box and extract the fraudulent token: `CL34R4NC3_0V3RR1D3`.
- Submit your recovered override flag:
  `FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}` *(also accepted: `CL34R4NC3_0V3RR1D3`)*.

---

## Flag Format
```
FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}
```
*Submit your verified override token on the Lab Portal to confirm the clearance breach!*
