import re

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "r") as f:
    code = f.read()

code = code.replace('#include "hwcrypto/sha.h"', '#include "mbedtls/sha1.h"')
code = code.replace('esp_sha(SHA1,', 'mbedtls_sha1(')

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "w") as f:
    f.write(code)

print("Patching SHA complete.")
