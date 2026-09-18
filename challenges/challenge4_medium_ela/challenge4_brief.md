# Challenge 4: Operation Rogue Credential (Medium)

## Incident Overview
**Classification:** INTERNAL SECURITY BREACH // CASE FILE #SEC-2026-089  
**Target File:** `evidence_clearance_badge.jpg`  
**Difficulty:** Medium  
**Theme:** Document Forensics & Error Level Analysis (ELA)

---

## Case Scenario
At 02:15 AM, security personnel at the High-Security Biometrics & Research Vault detained an individual attempting to enter the Special Access Program facility. The individual presented a laminated departmental security clearance badge (`evidence_clearance_badge.jpg`). 

Visually, the badge appears to grant **LEVEL 4 (TOP SECRET / SCI)** access with an official approval stamp and a digital crypto-override token.

However, a query to the central personnel database indicates the contractor was only ever granted **LEVEL 1 (RESTRICTED VISITOR)** privileges. Physical security suspects the badge image was digitally forged by compositing an unauthorized Level 4 credential patch prior to lamination.

As the forensic image analyst, your task is to perform **Error Level Analysis (ELA)** on the badge photograph to expose the digital forgery, identify the spliced region, and retrieve the rogue override token.

---

## Mission Objectives
1. Load `evidence_clearance_badge.jpg` into your forensic image analysis tool (such as GIMP or the included `offline_ela_viewer.html`).
2. Perform **Error Level Analysis (ELA)** across the badge.
3. Compare the compression error rate of the personal details, photograph, and barcode against the clearance section.
4. Confirm digital tampering and locate the forged authorization block.
5. Recover the digital crypto-override token embedded inside the forged region.
6. Submit the flag in the format: `FLAG{...}`

---

## Recommended Investigative Tools & Methods

### Method 1: Standalone Offline ELA Inspector
1. Open `offline_ela_viewer.html` in any web browser.
2. Ensure `evidence_clearance_badge.jpg` is loaded into the viewer.
3. Adjust the controls:
   - Set **Resave Quality:** `90%`
   - Set **Error Amplification:** `25x` to `30x`
4. Observe the difference in illumination across the document. Legitimate areas will settle into a dark, low-noise baseline, while the spliced clearance block will illuminate brightly.

### Method 2: Professional Forensic Analysis in GIMP
1. Open `evidence_clearance_badge.jpg` in GIMP.
2. Export a temporary copy: `File -> Export As... -> badge_resaved.jpg` with **Quality = 90%**.
3. Load the resaved image as a new layer: `File -> Open as Layers... -> badge_resaved.jpg`.
4. Set the blend mode of the top layer to **Difference**.
5. Merge or create a new layer from visible (`Layer -> New from Visible`), then amplify brightness: `Colors -> Brightness-Contrast` or `Colors -> Levels`.
6. Inspect the brightly glowing rectangular splice.

---

## Flag Format
```
FLAG{...}
```
*Submit your verified forensic flag to clear Case File #SEC-2026-089!*
