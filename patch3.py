import re

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "r") as f:
    code = f.read()

code = re.sub(r'const char \*wifi_ssid\s*=\s*".*?";', 'const char *wifi_ssid = "Snug as a Bug";', code)
code = re.sub(r'const char \*wifi_password\s*=\s*".*?";', 'const char *wifi_password = "Loop2loop@1337";', code)
code = re.sub(r'const char \*username\s*=\s*".*?";', 'const char *username = "micemeat";', code)

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "w") as f:
    f.write(code)

print("Patch 3 complete.")
