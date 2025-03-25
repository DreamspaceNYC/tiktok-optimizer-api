from flask import Flask, request, jsonify, send_file
import yt_dlp
import os
import subprocess
import uuid

app = Flask(__name__)
OUTPUT_FOLDER = "./outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def is_viral(metadata):
    title = metadata.get("title", "").lower()
    duration = metadata.get("duration", 999)
    resolution = metadata.get("height", 0)

    keywords = ["asmr", "prank", "story", "routine", "hack", "tiktok"]
    has_keywords = any(kw in title for kw in keywords)
    short = duration < 90
    vertical = resolution >= 720

    return short and has_keywords and vertical

def optimize_video(input_path, output_path):
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vf", "scale=720:-2",
        "-b:v", "1.5M",
        "-preset", "fast",
        "-movflags", "+faststart",
        output_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

@app.route("/api/tiktok")
def process():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing url param"}), 400

    uid = str(uuid.uuid4())
    raw = f"outputs/{uid}.raw.mp4"
    final = f"outputs/{uid}.final.mp4"

    ydl_opts = {
        "quiet": True,
        "outtmpl": raw,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "merge_output_format": "mp4"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        if is_viral(info):
            os.rename(raw, final)
        else:
            optimize_video(raw, final)
            os.remove(raw)

        return send_file(final, mimetype="video/mp4")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)