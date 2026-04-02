import re

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "r") as f:
    code = f.read()

# Remove includes
code = re.sub(r'#include <SPI\.h>', '// #include <SPI.h>', code)
code = re.sub(r'#include <Wire\.h>', '// #include <Wire.h>', code)
code = re.sub(r'#include <Adafruit_GFX\.h>', '// #include <Adafruit_GFX.h>', code)
code = re.sub(r'#include <Adafruit_SSD1306\.h>', '// #include <Adafruit_SSD1306.h>', code)

# Remove display definitions
code = re.sub(r'#define SCREEN_WIDTH 128', '// #define SCREEN_WIDTH 128', code)
code = re.sub(r'#define SCREEN_HEIGHT 32', '// #define SCREEN_HEIGHT 32', code)
code = re.sub(r'#define OLED_RESET\s+4', '// #define OLED_RESET 4', code)
code = re.sub(r'#define SCREEN_ADDRESS 0x3C', '// #define SCREEN_ADDRESS 0x3C', code)
code = re.sub(r'Adafruit_SSD1306 display.*?;', '// Adafruit_SSD1306 display;', code)

# Remove display setup
code = re.sub(r'display\.begin\(SSD1306_SWITCHCAPVCC,\s*SCREEN_ADDRESS\);', '', code)
code = re.sub(r'display\.clearDisplay\(\);', '', code)
code = re.sub(r'display\.display\(\);', '', code)

# Find and replace the loop() function
# The loop() function is the last function in the file, we can just replace everything from "void loop() {" to the end.
# First, let's write a dummy loop() instead.
loop_start = code.find('void loop() {')
if loop_start != -1:
    code = code[:loop_start] + "void loop() {\n  delay(5000);\n}\n"

with open("DucoMiner-Monitor-ESP32/Duco_esp32_oled/Duco_esp32_oled.ino", "w") as f:
    f.write(code)

print("Patching complete.")
