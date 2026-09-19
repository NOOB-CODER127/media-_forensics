# Participant Walkthrough: Challenge 5 (Stereo Audio Forensics)

## Case: Operation Blackout Broadcast
- **Difficulty:** Medium
- **Forensic Tool:** Audacity
- **Target Evidence:** `covert_broadcast.wav` (Stereo 44.1kHz 16-bit)
- **Objective:** Separate independent stereo channels, perform spatial spectrogram analysis, and assemble the bifurcated passkey.

---

### Investigation Overview & Forensic Theory
Intelligence intercepted a short-wave clandestine broadcast (`covert_broadcast.wav`). Listening to the recording reveals multi-tonal electronic warbling and atmospheric interference.

#### Why Mono Spectrogram View Fails
In standard single-channel (mono) audio steganography, all frequency data exists on a single plane. However, `covert_broadcast.wav` was recorded in **two-channel stereo**:
- The transmitting operative hid the first half of the secret key in the **Left Audio Channel** and the second half in the **Right Audio Channel**.
- Both halves were encoded in the exact same frequency band (6 kHz – 12 kHz) during the exact same time window (3.0s – 15.0s).
- If you view the file as a single merged stereo track, the letter strokes from both channels print on top of each other, creating an unintelligible, scrambled blur.
- To solve this challenge, you must perform **Spatial Channel Decoupling** to inspect the Left and Right channels independently.

---

### Step-by-Step Solution in Audacity

#### Step 1: Open the Stereo Evidence
1. Launch **Audacity**.
2. Go to `File -> Open...` and select `covert_broadcast.wav`.
3. In the track header on the left, note that it specifies **Stereo, 44100Hz 16-bit**.

#### Step 2: Decouple the Stereo Channels
1. Locate the downward chevron `▼` next to the track name `covert_broadcast` on the left control panel.
2. Click `▼` and select **Split Stereo Track**.
3. Audacity immediately splits the file into two independent tracks:
   - **Top Track:** Left Channel (Pan: 100% Left)
   - **Bottom Track:** Right Channel (Pan: 100% Right)

#### Step 3: Configure Spectrogram on Track 1 (Left Channel)
1. On the **Top Track** (Left Channel), click the chevron `▼` and select **Spectrogram**.
2. Click the chevron `▼` again and select **Spectrogram Settings...**:
   - **Scale:** Change from `Logarithmic` to **`Linear`** *(Crucial)*
   - **Window size:** `1024` or `2048`
   - **Max Frequency (Hz):** `14000`
   - **Min Frequency (Hz):** `5000`
3. Click **OK** (or **Apply**).
4. Zoom in horizontally across the timeline between **2.5 seconds and 15.5 seconds** (`Ctrl + 1` or `Ctrl + Mouse Wheel`).
5. A clear white luminous box appears in the frequency spectrum displaying **Part 1** of the flag:
```
+------------------------------------+
|  FLAG{DU4L_CH4NN3L_                |
+------------------------------------+
```

#### Step 4: Configure Spectrogram on Track 2 (Right Channel)
1. On the **Bottom Track** (Right Channel), click the chevron `▼` and select **Spectrogram**.
2. Click the chevron `▼` again and select **Spectrogram Settings...**:
   - **Scale:** Change from `Logarithmic` to **`Linear`**
   - **Window size:** `1024` or `2048`
   - **Max Frequency (Hz):** `14000`
   - **Min Frequency (Hz):** `5000`
3. Click **OK** (or **Apply**).
4. Scroll horizontally to the same time window (2.5s to 15.5s).
5. A distinct white luminous box appears in the right frequency spectrum displaying **Part 2** of the flag:
```
+------------------------------------+
|  ST3R30_SP3CTRUM}                  |
+------------------------------------+
```

#### Step 5: Assemble the Secret Passkey
Concatenate the two recovered segments together:
- **Left Track (Part 1):** `FLAG{DU4L_CH4NN3L_`
- **Right Track (Part 2):** `ST3R30_SP3CTRUM}`
- **Complete Passkey:**
```
FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}
```

#### Step 6: Flag Verification
Submit the concatenated token in the Lab Portal:
```
FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}
```
Validation confirms both channels have been successfully recovered!
