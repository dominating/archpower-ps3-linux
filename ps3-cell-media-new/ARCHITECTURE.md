# PS3 Cell Media - Jellyfin & YouTube Client

## Overview
A lightweight, hardware-accelerated media client for the PS3 (Cell Broadband Engine). 
Built using the PSL1GHT toolchain and SDL2, designed to bypass the heavy, laggy web wrappers of the official apps.

## Architecture Pipeline

1. **UI & Input (SDL2)**
   - Renders a clean 720p/1080p interface via RSX.
   - Captures DualShock 3 inputs via `io/pad.h` wrapper in SDL.

2. **Networking (libcurl + cJSON)**
   - **YouTube:** Communicates with an Invidious API instance to scrape video streams without needing heavy Google JS/bloat.
   - **Jellyfin:** Uses standard Jellyfin REST API for auth, library browsing, and direct stream URL generation.

3. **Video Decoding (FFmpeg/libavcodec)**
   - Re-uses our `libps3rp` shared library logic. 
   - Pulls HLS/mp4 streams and feeds them into the AV pipeline, converting YUV frames to RGB textures for SDL2 to present on screen.

## Goals
- Sub-50MB RAM footprint (leaving plenty of memory for the frame buffer).
- Snappy 60FPS UI navigation.
- No background telemetry.
