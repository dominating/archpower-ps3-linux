import sys

with open('depin-hub/guides/nerdminer-digibyte.md', 'r') as f:
    content = f.read()

pre = content.split("## 3. Flashing the Firmware")[0]
post = content.split("## 4. Configuration")[1]

new_flash = """## 3. Flashing the Firmware

You do not need to install Python or use the command line (`esptool.py`) to flash your ESP32-S2. You can flash the compiled `.bin` file directly from your browser.

1. Download the custom compiled firmware from the DePIN Hub homepage.
2. Open Google Chrome or Microsoft Edge (Safari/Firefox do not support Web Serial).
3. Go to the official **[Espressif Web Flasher (esptool-js)](https://espressif.github.io/esptool-js/)**.
4. Plug your ESP32-S2 into your computer via USB. *(If it's not recognized, hold the `BOOT` button on the board while plugging it in).*
5. Change the **Baudrate** dropdown to `460800`.
6. Click the **Connect** button and select the USB/COM port for your ESP32 from the browser popup.
7. In the **Program** section that appears:
   - Set the **Flash Address** to `0x0`.
   - Click **Choose File** and select your downloaded `nerdminer-dgb-merged.bin` file.
8. Click **Program** and wait for the progress bar to reach 100%.

"""

with open('depin-hub/guides/nerdminer-digibyte.md', 'w') as f:
    f.write(pre + new_flash + "## 4. Configuration" + post)

print("Success")
