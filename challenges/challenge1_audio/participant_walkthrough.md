# Participant Walkthrough: Challenge 1 (Audio Forensics)

## Case: Operation Whispering Wiretap
- **Difficulty:** Easy
- **Forensic Tool:** Audacity (or Sonic Visualiser)
- **Target Evidence:** `intercepted_wiretap.wav`
- **Objective:** Recover the hidden visual passphrase encoded in the high-frequency radio spectrum.

---

### Investigation Overview & Theory
When listening to `intercepted_wiretap.wav`, you only hear atmospheric static, powerline hum, and radio interference. Covert operatives frequently use **Spectrogram Steganography** to hide visual data above normal voice frequencies (>8 kHz) where human ears perceive it as ordinary hiss.

A **spectrogram** converts audio into a visual graph:
- **Horizontal Axis (X):** Time (seconds)
- **Vertical Axis (Y):** Frequency (Hertz / kHz)
- **Color Intensity (Z):** Volume / Amplitude (dB)

---

### Step-by-Step Solution in Audacity

#### Step 1: Open Evidence in Audacity
1. Launch **Audacity**.
2. Go to `File -> Open...` and select `intercepted_wiretap.wav`.
3. The track initially displays as a blue **Waveform** (showing volume over time). Playing the file reveals ordinary radio noise.

#### Step 2: Switch to Spectrogram View
1. Look at the track header panel on the left side of the screen (where the track name `intercepted_wiretap` is located).
2. Click the downward chevron arrow `▼` next to `intercepted_wiretap`.
3. Select **Spectrogram** from the dropdown menu.
4. You will see colored frequency bands across the timeline, with faint shapes visible near the top border.

#### Step 3: Calibrate Spectrogram Settings (Linear Scale)
*By default, Audacity uses a Logarithmic scale which squishes high frequencies at the very top of the track. We must switch to a Linear scale.*

1. Click the downward chevron `▼` on the track header again.
2. Select **Spectrogram Settings...**.
3. Configure the following parameters:
   - **Scale:** Change from `Logarithmic` to **`Linear`** *(Critical)*
   - **Window size:** `1024` or `2048`
   - **Max Frequency (Hz):** `16000` (or `20000`)
   - **Min Frequency (Hz):** `7000` (or `0`)
4. Click **OK** (or **Apply**).

#### Step 4: Zoom into the Message Timeline
1. Use the Zoom tool (`Ctrl + 1` to zoom in, or hold `Ctrl` and scroll your mouse wheel).
2. Scroll horizontally to the section between **2.5 seconds and 14.5 seconds**.
3. You will see crisp, luminous alphanumeric characters rendered directly into the frequency band between 9,000 Hz and 14,500 Hz:

```
+------------------------------------+
|  FLAG{SP3CTR4L_AUD10_CYPH3R}      |
+------------------------------------+
```

#### Step 5: Flag Verification
Submit the extracted string:
```
FLAG{SP3CTR4L_AUD10_CYPH3R}
```
Validate it in the Lab Portal to confirm your solve and claim your prize token!
