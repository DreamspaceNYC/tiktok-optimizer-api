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