# TikTok Optimizer API

This project is a lightweight video processor built to automatically download videos (YouTube, Vimeo, etc.), evaluate their metadata for TikTok virality potential, and optimize them using FFmpeg before serving them back via an API.

## Features

- Download videos via `yt-dlp`
- Analyze metadata (title, duration, resolution)
- Auto-optimize video for TikTok (720p, small file size, fast start)
- FFmpeg-based video enhancements
- Simple Flask API
- Deployable via Railway (Docker-based)

## API Endpoint

### Response:
Returns the optimized `.mp4` file if successful.

### Errors:
- `400`: Missing URL parameter
- `500`: Video fetch or optimization error

## Deployment

To deploy:

```bash
# Clone the repo
git clone https://github.com/hack-codes/yt-ffmpeg-tiktok.git
cd yt-ffmpeg-tiktok

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
