# Challenge 5: Operation Blackout Broadcast (Medium)

## Incident Overview
**Classification:** CLANDESTINE PIRATE TRANSMISSION // LOG #SIGINT-2026-92  
**Target Audio:** `covert_broadcast.wav`  
**Difficulty:** Medium  
**Theme:** Stereo Audio Forensics & Multi-Channel Spatial Spectrogram

---

## Case Scenario
Signals Intelligence (SIGINT) intercepted an 18-second audio recording (`covert_broadcast.wav`) transmitted over a clandestine pirate radio frequency. The transmission sounds like an atmospheric numbers-station broadcast: deep synthesizer drones, tape hiss, and subtle harmonic pulses.

Preliminary spectral scans suggest that a covert operative transmitted a secret two-part passkey. However, opening the recording as a standard mono track produces a cluttered, illegible visual spectrogram because the operative used **spatial frequency multiplexing** across separate stereo channels.

As a digital forensic audio analyst, your objective is to isolate the individual audio channels, configure optimal spectrogram view parameters, and recover the two halves of the encrypted passphrase.

---

## Mission Objectives
1. Import `covert_broadcast.wav` into an audio forensics tool (e.g., **Audacity** or **Sonic Visualiser**).
2. Note that the file is a **2-Channel Stereo** recording.
3. **Decouple the stereo channels** (in Audacity: click the track dropdown and choose `Split Stereo Track`).
4. Switch both individual tracks to **Spectrogram View** with **Linear Scale** focusing on the **6,000 Hz – 12,000 Hz** frequency band.
5. Extract **Part 1** from the **Left Channel** and **Part 2** from the **Right Channel**.
6. Concatenate the two halves together to assemble the full passphrase.
7. Submit the flag in the format: `FLAG{...}`

---

## Recommended Investigative Tools & Methods

### Method 1: Audacity (Portable / Desktop)
1. Open Audacity and import `covert_broadcast.wav` (`File -> Open...`).
2. Notice the track has two waveforms (Top = Left Channel, Bottom = Right Channel).
3. Click the downward chevron `▼` next to the track title (`covert_broadcast`) on the left control panel.
4. Select **Split Stereo Track** (or `Split Stereo to Mono`). This separates the channels into two completely independent tracks.
5. For **Track 1 (Left Channel)**:
   - Click the track dropdown chevron `▼` and select **Spectrogram**.
   - Click the chevron `▼` again -> **Spectrogram Settings...**.
   - Set **Scale:** `Linear`, **Max Frequency:** `14000 Hz`, **Min Frequency:** `5000 Hz`.
   - Read the first half of the secret flag: `FLAG{..._`
6. For **Track 2 (Right Channel)**:
   - Click the track dropdown chevron `▼` and select **Spectrogram**.
   - Apply the same Linear Spectrogram settings (5,000 Hz – 14,000 Hz).
   - Read the second half of the secret flag: `...}`
7. Concatenate both halves together.

---

## Flag Format
```
FLAG{...}
```
*Submit your verified secret passkey to the Zone Lead or via the Lab Portal!*
