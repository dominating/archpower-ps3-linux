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
