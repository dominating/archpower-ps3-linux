# ESP32-S2 Digibyte Mining Guide (NerdMiner V2/NM-TV)

This guide walks through flashing an ESP32-S2 dongle with NerdMiner V2 (or NM-TV) firmware, configured to connect to a Digibyte (DGB) SHA-256 solo or low-hash pool. 

While NerdMiner is typically used for Bitcoin lotteries, Digibyte's multi-algo approach includes SHA-256, allowing these ultra-low-power devices to mine DGB directly on compatible pools.

## 1. Requirements

- ESP32-S2 USB Dongle (or any ESP32-S2/S3 board)
- A PC/Mac/Linux machine for flashing
- Chrome/Edge browser (for Web Flasher) OR `esptool.py` installed
- A Digibyte Wallet Address (e.g., from an exchange or official DGB wallet)

## 2. Choosing a Pool

You need a pool that supports low-difficulty SHA-256 for Digibyte. Solo mining or standard DGB pools can be used depending on network difficulty.
Example pools:
- `sha256.dgb256.online:3333` (Example solo/low diff pool)
- `stratum+tcp://sha256.eu.mine.zergpool.com:3434` (Auto-exchange pools that pay out in DGB)

*Check miningpoolstats.stream/digibyte-sha256 for active SHA-256 DGB pools.*

## 3. Flashing the Firmware

### Option A: Web Flasher (Easiest)
1. Go to the [NerdMiner Web Flasher](https://flasher.bitronics.store/).
2. Select **NerdMinerV2** and your board type (**ESP32-S2**).
3. Connect your ESP32-S2 via USB while holding the `BOOT` button (to enter download mode).
4. Click **Flash**, select the COM port, and wait for completion.

### Option B: Command Line (esptool)
If you downloaded the compiled `.bin` file:
```bash
esptool.py -p /dev/ttyACM0 -b 460800 --before default_reset --after hard_reset --chip esp32s2 write_flash --flash_mode dio --flash_freq 80m --flash_size 4MB 0x10000 merged_nm_v2_s2.bin
```

## 4. Configuration

1. After flashing, unplug and replug the ESP32-S2.
2. Connect to the new Wi-Fi network: **NerdMinerAP** (Password: `MineYourCoins`).
3. A captive portal will pop up. If not, browse to `192.168.4.1`.
4. Enter your configuration:
   - **SSID & Password:** Your local Wi-Fi network credentials.
   - **Pool URL:** `sha256.eu.mine.zergpool.com`
   - **Pool Port:** `3434`
   - **Your BTC/DGB Address:** Your Digibyte Wallet Address (Note: some pools like Zergpool require putting your payout coin in the password field: `c=DGB`). If mining directly to a DGB SHA256 pool, just use your DGB address as the username.
   - **Password:** `c=DGB,mc=DGB` (if using auto-exchange pool) or `x` for standard pools.

5. Click **Save** and wait for the device to reboot.

## 5. Monitoring

Your ESP32-S2 will now connect to your Wi-Fi and begin hashing. The NM-TV interface (or standard NerdMiner screen if using a board with a display) will show your current hash rate (typically ~40-60 kH/s on ESP32-S2). 

Check your pool's dashboard by entering your wallet address to see live statistics and payouts.