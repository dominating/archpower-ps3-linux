import re

with open("depin-hub/index.html", "r") as f:
    html = f.read()

guide_html = """
<!-- Featured Guide -->
<section class="mb-20 bg-[#161b22] border border-[#58a6ff] rounded-2xl p-8 relative overflow-hidden shadow-[0_0_20px_rgba(88,166,255,0.1)]">
    <div class="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-[#58a6ff]/10 rounded-full blur-3xl z-0"></div>
    <div class="relative z-10 flex flex-col md:flex-row gap-8 items-center">
        <div class="w-full md:w-1/2">
            <h3 class="text-3xl font-extrabold text-white mb-4"><span class="gradient-text">Featured Guide:</span> DuinoCoin ESP32-S2 USB Miner</h3>
            <p class="text-gray-300 mb-6 leading-relaxed">Turn your ESP32-S2 USB Dongle into a dedicated <a href="https://duinocoin.com/" class="text-[#58a6ff] hover:underline" target="_blank">DuinoCoin (DUCO)</a> miner! We've compiled a lightweight, headless (no-monitor) firmware that drops right onto your device for silent, passive hashing.</p>
            
            <div class="bg-[#0d1117] rounded-xl p-5 border border-[#30363d] mb-6">
                <h4 class="text-white font-bold mb-3 flex items-center">
                    <svg class="w-5 h-5 mr-2 text-[#3fb950]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    Quick Start
                </h4>
                <ol class="list-decimal list-inside text-sm text-gray-400 space-y-3">
                    <li><a href="/firmware/s2/duco/merged.bin" class="text-[#58a6ff] hover:underline font-mono bg-[#58a6ff]/10 px-1 rounded">Download merged.bin</a></li>
                    <li>Plug your ESP32-S2 USB Dongle into your computer.</li>
                    <li>Flash the firmware using <code class="text-[#f5a90f] bg-[#f5a90f]/10 px-1 rounded">esptool.py</code> to offset <code class="text-white">0x0</code>:
                        <div class="mt-2 bg-black p-3 rounded-lg border border-[#30363d] overflow-x-auto text-xs text-green-400 font-mono">
                            esptool.py -p /dev/ttyACM0 -b 460800 write_flash 0x0 merged.bin
                        </div>
                    </li>
                    <li class="pt-1 italic">Note: Replace <code class="text-white">/dev/ttyACM0</code> with your COM port on Windows (e.g., <code class="text-white">COM3</code>).</li>
                </ol>
            </div>
            <div class="flex items-center space-x-4">
                <span class="badge badge-device text-xs px-3 py-1">ESP32-S2</span>
                <span class="badge badge-windows text-xs px-3 py-1">Headless</span>
            </div>
        </div>
        
        <div class="w-full md:w-1/2 rounded-xl overflow-hidden border border-[#30363d] shadow-lg relative aspect-[16/9] bg-black flex items-center justify-center">
            <!-- Promo Video Placeholder -->
            <video id="promo-video" class="w-full h-full object-cover" controls autoplay loop muted playsinline poster="https://duinocoin.com/assets/img/duco.png">
                <source src="/assets/videos/duco-promo.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
</section>
"""

# Insert right after the header section text (before Section 1)
split_marker = "<!-- Section 1: Free / Zero Investment -->"
parts = html.split(split_marker)
if len(parts) > 1:
    new_html = parts[0] + guide_html + "\n" + split_marker + parts[1]
    with open("depin-hub/index.html", "w") as f:
        f.write(new_html)
    print("Injected guide HTML.")
else:
    print("Could not find split marker.")
