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
1. Load `crime_scene_evidence.jpg` into your forensic image analysis tool (such as GIMP or the included `offline_ela_viewer.html`).
2. Perform **Error Level Analysis (ELA)** across the crime scene.
3. **Overcome Forensic Red Herrings:** Natural high-contrast edges (like the yellow marker cones A and B, or the black censor bar over the eyes) naturally generate high-frequency compression edges. Distinguish between normal edge frequency response and **true areal compression manipulation**.
4. Identify the staged physical evidence item that exhibits an unnatural compression error rate across its entire surface.
5. Inspect the staged item and retrieve the official forensic evidence token.
6. Submit the flag in the format: `FLAG{...}`

---

## Recommended Investigative Methods

### Method 1: Standalone Offline ELA Inspector
1. Open `offline_ela_viewer.html` in your web browser.
2. Ensure `crime_scene_evidence.jpg` is loaded.
3. Set **Resave Quality:** `90%` and **Error Amplification:** `30x`.
4. Scan the floor, the body, the blood pools, the markers, and the weapon.
5. Note which item glows with distinct, multi-colored high error levels across its entire body compared to the surrounding wooden floor and blood.

### Method 2: Professional Forensic Analysis in GIMP
1. Open `crime_scene_evidence.jpg`.
2. Export a temporary copy: `File -> Export As... -> temp_ela.jpg` at **Quality: 90%**.
3. Load the copy back as a layer: `File -> Open as Layers... -> temp_ela.jpg`.
4. Change the top layer mode to **Difference**.
5. Create a new layer from visible (`Layer -> New from Visible`), then boost brightness: `Colors -> Brightness-Contrast` or `Colors -> Levels`.
6. Zoom into the glowing region.

---

## Flag Format
```
FLAG{...}
```
*Submit your verified forensic flag to complete Case 1 and clear the investigation!*
