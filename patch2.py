import re

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "r") as f:
    code = f.read()

code = code.replace('#include <WiFi.h>', '#include <WiFi.h>\n#include <WiFiClientSecure.h>')
code = code.replace('btStop();', '// btStop();')
code = code.replace('esp_task_wdt_init(WDT_TIMEOUT, true);', '// esp_task_wdt_init();')

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "w") as f:
    f.write(code)

print("Patch 2 complete.")
