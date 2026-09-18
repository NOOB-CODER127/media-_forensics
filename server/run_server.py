#!/usr/bin/env python3
"""
Media Forensics & Deepfake Lab - Local Event Server
Launches the offline distribution portal and flag validation interface.
Automatically prepares zip archives for one-click downloading over local Wi-Fi.
"""

import os
import sys
import socket
import zipfile
import http.server
import socketserver
import argparse

PORT = 8000
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
DOWNLOADS_DIR = os.path.join(PUBLIC_DIR, "downloads")

# Official Flags
FLAGS = {
    "ch1": "FLAG{SP3CTR4L_AUD10_CYPH3R}",           # Easy: Audio Spectrogram
    "ch2": "FLAG{PL4T3_VB698108_CLR}",              # Medium: Video De-blur (Toyota Camry)
    "ch3": "FLAG{3L4_ST4G3D_W34P0N_R3V0LV3R}",      # Hard: Crime Scene ELA
    "ch4": "FLAG{3L4_R0GU3_CL34R4NC3_0V3RR1D3}",      # Medium: Document ELA
    "ch5": "FLAG{DU4L_CH4NN3L_ST3R30_SP3CTRUM}",    # Medium: Stereo Spectrogram
}

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def build_zip_package(zip_path, file_mappings):
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arc in file_mappings:
            if os.path.isdir(src):
                for root, _, files in os.walk(src):
                    for f in files:
                        full_path = os.path.join(root, f)
                        rel_path = os.path.relpath(full_path, src)
                        zf.write(full_path, os.path.join(arc, rel_path))
            elif os.path.exists(src):
                zf.write(src, arc)

def prepare_downloads():
    print("[*] Preparing distribution zip archives...")
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)

    ch1_dir = os.path.join(BASE_DIR, "challenges", "challenge1_audio")
    ch2_dir = os.path.join(BASE_DIR, "challenges", "challenge2_video")
    ch3_dir = os.path.join(BASE_DIR, "challenges", "challenge3_ela")
    ch4_dir = os.path.join(BASE_DIR, "challenges", "challenge4_medium_ela")
    ch5_dir = os.path.join(BASE_DIR, "challenges", "challenge5_medium_audio")

    os.system(f"cp {os.path.join(ch3_dir, 'crime_scene_evidence.jpg')} {PUBLIC_DIR}/crime_scene_evidence.jpg 2>/dev/null || true")
    os.system(f"cp {os.path.join(ch3_dir, 'offline_ela_viewer.html')} {PUBLIC_DIR}/ela_tool.html 2>/dev/null || true")

    # Challenge 1 (Audio - Easy)
    build_zip_package(
        os.path.join(DOWNLOADS_DIR, "challenge1_audio.zip"),
        [
            (os.path.join(ch1_dir, "intercepted_wiretap.wav"), "intercepted_wiretap.wav"),
            (os.path.join(ch1_dir, "challenge1_brief.md"), "challenge1_brief.md"),
        ]
    )

    # Challenge 2 (Video - Medium)
    build_zip_package(
        os.path.join(DOWNLOADS_DIR, "challenge2_video.zip"),
        [
            (os.path.join(ch2_dir, "surveillance_traffic.mp4"), "surveillance_traffic.mp4"),
            (os.path.join(ch2_dir, "challenge2_brief.md"), "challenge2_brief.md"),
            (os.path.join(ch2_dir, "frames"), "frames"),
        ]
    )

    # Challenge 3 (Crime Scene ELA - Hard)
    build_zip_package(
        os.path.join(DOWNLOADS_DIR, "challenge3_crime_scene_ela.zip"),
        [
            (os.path.join(ch3_dir, "crime_scene_evidence.jpg"), "crime_scene_evidence.jpg"),
            (os.path.join(ch3_dir, "challenge3_brief.md"), "challenge3_brief.md"),
            (os.path.join(ch3_dir, "offline_ela_viewer.html"), "offline_ela_viewer.html"),
        ]
    )

    # Challenge 4 (Document ELA - Medium)
    build_zip_package(
        os.path.join(DOWNLOADS_DIR, "challenge4_medium_ela.zip"),
        [
            (os.path.join(ch4_dir, "evidence_clearance_badge.jpg"), "evidence_clearance_badge.jpg"),
            (os.path.join(ch4_dir, "challenge4_brief.md"), "challenge4_brief.md"),
            (os.path.join(ch4_dir, "offline_ela_viewer.html"), "offline_ela_viewer.html"),
        ]
    )

    # Challenge 5 (Stereo Audio Spectrogram - Medium)
    build_zip_package(
        os.path.join(DOWNLOADS_DIR, "challenge5_medium_audio.zip"),
        [
            (os.path.join(ch5_dir, "covert_broadcast.wav"), "covert_broadcast.wav"),
            (os.path.join(ch5_dir, "challenge5_brief.md"), "challenge5_brief.md"),
        ]
    )

    # Complete Bundle
    build_zip_package(
        os.path.join(DOWNLOADS_DIR, "all_challenges_bundle.zip"),
        [
            (os.path.join(ch1_dir, "intercepted_wiretap.wav"), "challenge1_audio/intercepted_wiretap.wav"),
            (os.path.join(ch1_dir, "challenge1_brief.md"), "challenge1_audio/challenge1_brief.md"),
            (os.path.join(ch2_dir, "surveillance_traffic.mp4"), "challenge2_video/surveillance_traffic.mp4"),
            (os.path.join(ch2_dir, "challenge2_brief.md"), "challenge2_video/challenge2_brief.md"),
            (os.path.join(ch2_dir, "frames"), "challenge2_video/frames"),
            (os.path.join(ch3_dir, "crime_scene_evidence.jpg"), "challenge3_ela/crime_scene_evidence.jpg"),
            (os.path.join(ch3_dir, "challenge3_brief.md"), "challenge3_brief.md"),
            (os.path.join(ch3_dir, "offline_ela_viewer.html"), "challenge3_ela/offline_ela_viewer.html"),
            (os.path.join(ch4_dir, "evidence_clearance_badge.jpg"), "challenge4_medium_ela/evidence_clearance_badge.jpg"),
            (os.path.join(ch4_dir, "challenge4_brief.md"), "challenge4_medium_ela/challenge4_brief.md"),
            (os.path.join(ch4_dir, "offline_ela_viewer.html"), "challenge4_medium_ela/offline_ela_viewer.html"),
            (os.path.join(ch5_dir, "covert_broadcast.wav"), "challenge5_medium_audio/covert_broadcast.wav"),
            (os.path.join(ch5_dir, "challenge5_brief.md"), "challenge5_medium_audio/challenge5_brief.md"),
            (os.path.join(BASE_DIR, "handouts", "Participant_Brief_and_CheatSheet.md"), "Participant_CheatSheet.md"),
        ]
    )
    print("[+] Zip archives ready in server/public/downloads/")

class ForensicPortalHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def log_message(self, format, *args):
        sys.stdout.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format%args}\n")

def run_server(port=PORT):
    prepare_downloads()
    ip = get_lan_ip()
    
    print("\n" + "=" * 70)
    print(" MEDIA FORENSICS & DEEPFAKE LAB — LOCAL DISTRIBUTION PORTAL")
    print("=" * 70)
    print(f"  [+] Host Machine LAN IP:  {ip}")
    print(f"  [+] Server Listening on:  http://{ip}:{port}/")
    print(f"  [+] Localhost Access:     http://127.0.0.1:{port}/")
    print("=" * 70)
    print(f" Tell participants to connect to Zone Wi-Fi and open:")
    print(f"  >>> http://{ip}:{port}/ <<<")
    print("=" * 70)
    print(" Press Ctrl+C to shut down the server.\n")

    with socketserver.TCPServer(("", port), ForensicPortalHandler) as httpd:
        httpd.allow_reuse_address = True
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Server shutdown safely.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Media Forensics Local Portal Server")
    parser.add_argument("--port", type=int, default=PORT, help="Port to serve on (default: 8000)")
    parser.add_argument("--test", action="store_true", help="Prepare archives and verify directory without blocking")
    args = parser.parse_args()

    if args.test:
        prepare_downloads()
        print("[✓] Pre-flight server check passed!")
        sys.exit(0)
    else:
        run_server(args.port)
