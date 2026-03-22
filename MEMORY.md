# PassivePin & DePIN Operations - Long-Term Memory

## Key Learnings & Project Facts
- **Entropy (ESP32-S2)**: Enforces hardware lock-in using mTLS on their MQTT broker (`mqtts://mqtt.justentropy.lol:8883`). Self-signed certificates allow compilation but fail the TLS handshake, making it impossible to mine the memecoin without official keys from their portal. The `entropy-zero-fw` repository and binaries were deleted due to this limitation.
- **DuinoCoin (ESP32-S2)**: Successfully ported the `cifertech/DucoMiner-Monitor-ESP32` miner to the ESP32-S2 platform. Removed all OLED/monitor dependencies (`Adafruit_GFX`, `Adafruit_SSD1306`, I2C calls) to allow for stable, headless operation. Binaries (`merged.bin`, etc.) compiled via Arduino CLI (`esp32:esp32:esp32s2`) and hosted on the Vercel deployment at `/firmware/s2/duco/`. Configured to use generic `YOUR_WIFI_SSID`/`YOUR_WIFI_PASSWORD` for public distribution.
- **Vercel Deployment**: Vercel CLI (`vercel --prod --yes`) is used to manually push site updates and binary assets directly from the `depin-hub` directory.

## User Context
- **Name**: Jordan (Moltbook Email: micemeat1337@proton.me, Telegram: `5269660297`).
- **Goal**: Maintain "PassivePin", a DePIN & Airdrop directory website (`depin-hub.vercel.app`).
- **Preferences**: Headless operations, dark-mode crypto-native aesthetic, prefers open-source or free-to-run DePIN extensions/nodes.
- **Privacy**: Wi-Fi credentials and personal wallet addresses should not be exposed in public firmware or Vercel deployments.

## Active Systems
- **Auto-Scout Loop**: Configured via `HEARTBEAT.md` to run every 24 hours. Scouts new DePIN projects using `web_search`, notifies via Telegram, and automatically writes guides/deploys to Vercel upon approval.
- **Video Generator**: Remotion skill is installed and configured for programmatic motion graphics (`skills_log.md`), though currently not displaying correctly on the main `depin-hub` page.
- **Jordan Homepage**: Built and deployed a CiferTech-inspired cyberpunk/minimalist homepage at jordan-homepage-sigma.vercel.app, linking back to the DePIN Hub.

## Recent 2026-03-16 Insights
- **DePIN Hub UI Update**: Converted bulky DePIN Hub HTML cards to a spreadsheet-friendly table layout matching the CiferTech-inspired aesthetic of the personal homepage.
- **Auto-Scout Executed**: Deployed guides for DataHive AI, YOM Network, and Titan Network to the hub. Established a 24-hour Scout loop via HEARTBEAT.md.

## Recent 2026-03-17/18 Insights
- **PS3 Remote Play Port**: Began porting `open-rp` to modern C/C++ for Chiaki integration. Isolated auth and crypto logic.
- **ESP32-S2 Mining**: Built an optimized NerdMiner V2 firmware for the ZY ESP32-S2 to mine Digibyte (DGB) with dynamic thermal throttling at 75°C and aggressive `-O3` `-ffast-math` compilation flags. Hosted the binary (`nerdminer-dgb-merged.bin`) and guide on DePIN Hub. Also added a Nano (XNO) Unmineable-style guide via Prohashing (forcing `d=0.0001` difficulty to allow ESP32 hashing).
- **DuinoCoin**: Updated the DuinoCoin guide to utilize the `esptool-js` Web Flasher. Generated and delivered a hidden, hardcoded custom firmware for the user, then permanently deleted it.
- **Discord Scraper Skill**: Installed the `discord-intel` secure scraping pipeline. Received Bot Token `MTQ4MzYxMTYxMDIyMzIxODY4OA.GM6EgS.KUnL7VrFx1JW6xBZYfT2jM6PWaJddIW6v5PZrM`, currently waiting for the user to invite the bot to the target servers.
- **ARO Network**: Added ARO Network (Lite Node) to the DePIN Hub.

## Recent 2026-03-20 Insights
- **PS3 Remote Play Port**: Spun up a sub-agent to continue porting `open-rp` to modern C/C++ for Chiaki integration, focusing on HTTP logic and codecs renderer.
- **DePIN Hub Auto-Scout**: Discovered and added MyGate Network ($MYG) and DeepNode ($DN) to the PassivePin hub (`depin-hub.vercel.app`). Pushed updates locally and triggered a Vercel deployment without generating full Markdown guides, confirming the user's preference for fast, minimal executions for new additions unless requested otherwise.
