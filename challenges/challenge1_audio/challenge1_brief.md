# Challenge 1: Operation Whispering Wiretap (Easy)

## Incident Overview
**Classification:** TOP SECRET // COUNTER-ESPIONAGE LOG #SIGINT-2026-88  
**Target Audio:** `intercepted_wiretap.wav`  
**Allotted Time:** 30 Minutes  
**Difficulty:** Easy  
**Theme:** Audio Forensics & Spectrogram Steganography

---

## Case Scenario
Signals Intelligence (SIGINT) operators intercepted a suspicious 16-second radio transmission over an encrypted relay (`intercepted_wiretap.wav`). To the human ear, the recording appears to consist entirely of atmospheric noise, powerline hum, and radio static.

However, forensic acoustic analysis indicates unusual electromagnetic energy distributions in the high acoustic frequencies above human vocal speech. Forensic investigators believe a covert rendezvous passphrase was visually encoded directly into the sound frequencies using **Spectrogram Steganography**.

Your objective as a digital forensic investigator is to inspect the audio using spectral analysis software, calibrate the frequency display, and recover the concealed passphrase.

---

## Mission Objectives
1. Load `intercepted_wiretap.wav` into an audio spectral analysis tool (e.g., **Audacity**, **Sonic Visualiser**, or equivalent).
2. Switch the track view from conventional **Waveform** to **Spectrogram View**.
3. Adjust the spectrogram frequency scale and window settings to focus on the high-frequency band (**9,000 Hz – 15,000 Hz**).
4. Read the concealed visual flag characters drawn directly into the audio spectrum.
5. Submit the recovered flag in the format: `FLAG{...}`

---

## Recommended Investigative Tools & Methods

### Method 1: Audacity (Portable / Desktop)
1. Open Audacity and import `intercepted_wiretap.wav` (`File -> Open...`).
2. Click the downward chevron `▼` next to the track name (`intercepted_wiretap`) on the left track panel.
3. Select **Spectrogram** (replacing the default Waveform view).
4. To sharpen the visual text:
   - Click the track drop-down chevron `▼` again and choose **Spectrogram Settings...**.
   - Set **Algorithm:** `Spectrogram`
   - Set **Window size:** `1024` or `2048` (Hanning or Blackman)
   - Set **Max Frequency (Hz):** `16000` (or `20000`)
   - Set **Min Frequency (Hz):** `0` (or `7000`)
   - Set **Scale:** `Linear` (*Critical: Linear scale expands high frequencies so the text is not compressed at the top border*).
5. Zoom in horizontally across the timeline between **2.5s and 14.5s** (use `Ctrl + 1` or hold `Ctrl` and scroll mouse wheel).

### Method 2: Sonic Visualiser
1. Open `intercepted_wiretap.wav` in Sonic Visualiser.
2. Add a spectrogram pane: `Pane -> Add Spectrogram`.
3. Set the frequency scale to **Linear** in the right-hand layer properties panel.
4. Adjust the upper and lower frequency bounds to 7,000 Hz – 16,000 Hz.

---

## Flag Submission Format
```
FLAG{...}
```
*Submit your decrypted secret passkey to the Zone Lead or via the Lab Portal to claim your Challenge 1 Prize Token!*
