# Challenge 1 Walkthrough & Solution Guide

## Challenge Summary
- **Challenge Name:** Operation Whispering Wiretap
- **Difficulty:** Easy
- **Category:** Audio Forensics / Spectrogram Steganography
- **Target File:** `challenges/challenge1_audio/intercepted_wiretap.wav`
- **Official Flag:** `FLAG{SP3CTR4L_AUD10_CYPH3R}`

---

## Technical Background: Audio Spectrogram Steganography
A spectrogram is a 2D visual representation of the spectrum of frequencies of a signal as it varies with time. 
- The **X-axis** represents **Time** (in seconds).
- The **Y-axis** represents **Frequency** (in Hertz / kHz).
- The **Color / Intensity (Z-axis)** represents the **Amplitude / Power Spectral Density** (in dB).

By using the Inverse Short-Time Fourier Transform (iSTFT) or additive sinusoidal synthesis, an attacker or covert operative can deliberately place tone frequencies at specific time offsets such that the power spectrum forms readable visual shapes, symbols, or alphanumeric text. Because human hearing sensitivity drops significantly in the high-frequency band (above 10 kHz) and because speech energy is concentrated below 3.5 kHz, spectrogram text often sounds like high-pitched hiss, chirping, or subtle static.

---

## Step-by-Step Solution

### Step 1: Open Audio in Audacity
Launch Audacity and open `challenges/challenge1_audio/intercepted_wiretap.wav`.
When initially loaded, Audacity displays the conventional **Waveform**:
- The amplitude envelope shows steady background amplitude with slight noise fluctuations.
- Playing the audio produces an atmospheric radio static buzz with a faint 60Hz hum.

### Step 2: Switch to Spectrogram View
1. Click the downward chevron `▼` next to the track title **intercepted_wiretap** on the track control panel on the far left.
2. Select **Spectrogram** from the menu.
3. Observe that colored bands appear across the timeline. In the upper register (near the top of the track), a faint outline of letters is visible.

### Step 3: Optimize Audacity Spectrogram Settings
To make the text crisp and easily legible:
1. Click the track menu chevron `▼` again and choose **Spectrogram Settings...**.
2. Make the following adjustments:
   - **Scale:** Change from `Logarithmic` to **`Linear`** (essential: linear scale expands high frequencies so the text isn't compressed against the top border).
   - **Window size:** Set to **`1024`** or **`2048`**.
   - **Max Frequency:** Set to **`16000 Hz`** (or `20000 Hz`).
   - **Min Frequency:** Set to **`0 Hz`** or **`7000 Hz`** (zooms directly into the message band).
   - Click **Apply**.
3. Zoom in on the time range from **2.5s to 14.5s**.

### Step 4: Decipher the Hidden Message
A distinct, framed rectangular message appears rendered in luminous white/red frequency lines across the 9 kHz to 14.5 kHz range:
```
+------------------------------------+
|  FLAG{SP3CTR4L_AUD10_CYPH3R}      |
+------------------------------------+
```

Submitting this passphrase yields the final flag:
`FLAG{SP3CTR4L_AUD10_CYPH3R}`

---

## Facilitator Hint Progression
- **10 Minutes:** "You cannot solve this challenge by just listening with your ears. You need to visualize the sound frequencies over time."
- **18 Minutes:** "In Audacity, click the track name drop-down on the left and switch the view from 'Waveform' to 'Spectrogram'."
- **25 Minutes:** "Open 'Spectrogram Settings' in Audacity and switch the Scale from Logarithmic to 'Linear'. Look at the frequencies between 9,000 Hz and 15,000 Hz."
