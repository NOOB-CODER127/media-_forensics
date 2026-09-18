# Challenge 5 Walkthrough & Solution Guide

## Challenge Summary
- **Challenge Name:** Operation Blackout Broadcast
- **Difficulty:** Medium
- **Category:** Stereo Audio Forensics / Multi-Channel Spatial Spectrogram
- **Target File:** `challenges/challenge5_medium_audio/covert_broadcast.wav`
- **Official Flag:** `FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}`

---

## Technical Background: Spatial Channel Steganography
In standard single-channel (mono) audio steganography, all frequency energy occupies a single time-frequency plane. In stereo or multi-channel transmissions, audio forensics investigators must consider **channel independence**:
- Left and Right channels carry distinct signals.
- If viewed together as a merged or joint-stereo spectrogram, text drawn at the same time and frequency band in both channels overlaps and creates confusing, scrambled visual interference.
- By decoupling the channels (using Audacity's `Split Stereo Track` or programmatic array slicing `interleaved[0::2]` vs `interleaved[1::2]`), each channel reveals its dedicated payload cleanly.

---

## Step-by-Step Solution

### Step 1: Open Audio in Audacity
1. Launch Audacity and open `challenges/challenge5_medium_audio/covert_broadcast.wav`.
2. Notice that the track header displays **Stereo, 44100Hz 16-bit**.

### Step 2: Decouple Stereo Channels
1. Click the downward chevron `▼` next to the track name (`covert_broadcast`) on the far-left track control panel.
2. Select **Split Stereo Track**.
3. Audacity splits the audio into two separate independent tracks:
   - Upper track = **Left Channel**
   - Lower track = **Right Channel**

### Step 3: Calibrate Spectrograms for Both Channels
For each of the two tracks:
1. Click the track dropdown chevron `▼` -> choose **Spectrogram**.
2. Click the chevron `▼` again -> choose **Spectrogram Settings...**:
   - **Scale:** `Linear` *(Crucial)*
   - **Window size:** `1024` or `2048`
   - **Max Frequency:** `14000 Hz`
   - **Min Frequency:** `5000 Hz`
   - Click **Apply**.
3. Zoom in horizontally on the time range from **2.5s to 15.5s**.

### Step 4: Extract and Assemble the Passphrase
- **Left Channel Track:**
  A distinct framed white frequency box appears reading:
  ```
  FLAG{DU4L_CH4NN3L_
  ```
- **Right Channel Track:**
  A corresponding framed white frequency box appears reading:
  ```
  ST3R30_SP3CTRUM}
  ```
- **Assembly:**
  Concatenating Part 1 + Part 2 yields:
  ```
  FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}
  ```

---

### Automated Headless Verification
Run the automated solver:
```bash
python3 solutions/challenge5_medium_audio/solve_ch5_audio.py
```
Output:
```
[*] Running Stereo Audio Spectrogram Solver on: challenges/challenge5_medium_audio/covert_broadcast.wav
[+] Loaded Audio: 2 Channels (Stereo), 17.98s @ 44100Hz, 16-bit
[+] Rendered Left Channel Spectrogram:  solutions/challenge5_medium_audio/recovered_left_spectrogram.png
    [->] Left Channel Visual Segment:   'FLAG{DU4L_CH4NN3L_'
[+] Rendered Right Channel Spectrogram: solutions/challenge5_medium_audio/recovered_right_spectrogram.png
    [->] Right Channel Visual Segment:  'ST3R30_SP3CTRUM}'

[✓] STEREO CHANNEL DECOUPLING SUCCESSFUL!
[✓] ASSEMBLED COMPLETE SECRET PASSKEY: FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}
```

---

## Facilitator Hint Progression
- **@ 10 mins:** "Look at the track format in Audacity. Is this a mono audio file like Challenge 1, or is it stereo?"
- **@ 20 mins:** "If you view the spectrogram as a combined stereo track, the letters look scrambled because both channels are playing at once. You need to separate the channels."
- **@ 35 mins:** "Click the track menu drop-down on the left and select 'Split Stereo Track'. Look at the Left channel for part 1 and the Right channel for part 2."
