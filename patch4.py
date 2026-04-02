import re

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "r") as f:
    code = f.read()

code = re.sub(r'const char \*wifi_ssid\s*=\s*".*?";', 'const char *wifi_ssid = "YOUR_WIFI_SSID";', code)
code = re.sub(r'const char \*wifi_password\s*=\s*".*?";', 'const char *wifi_password = "YOUR_WIFI_PASSWORD";', code)

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "w") as f:
    f.write(code)

print("Patch 4 complete.")
