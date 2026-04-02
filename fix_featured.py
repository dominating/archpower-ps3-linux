import sys

with open('depin-hub/index.html', 'r') as f:
    content = f.read()

start_marker = '<!-- Featured Guide (Hardcoded for Digibyte/NerdMiner) -->'
end_marker = '<div class="mb-16 overflow-x-auto">'

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = content.split(end_marker)[1]
    
    new_html = """<!-- Featured Guide (Hardcoded for Digibyte/NerdMiner) -->
        <div class="w-full bg-[#111] border border-[#58a6ff]/30 p-6 mb-16 rounded-sm">
            <h3 class="text-xl font-bold text-[#58a6ff] uppercase tracking-widest mb-2">Featured: ESP32-S2 Digibyte Miner (NerdMiner V2)</h3>
            <p class="text-gray-400 text-sm mb-4">Optimized NM-TV/NerdMiner V2 firmware for the ZY ESP32-S2 USB Dongle (240MHz + Thermal Throttling @ 75°C). Configured for low-power SHA256 Digibyte (DGB) mining via solo/compatible pools.</p>
            <div class="flex items-center gap-4">
                <a href="/guides/nerdminer-digibyte.md" class="border border-[#58a6ff] text-[#58a6ff] text-xs font-bold px-4 py-2 hover:bg-[#58a6ff] hover:text-black transition uppercase">View Guide</a>
                <a href="/firmware/s2/nerdminer-dgb-merged.bin" class="bg-[#58a6ff] text-black text-xs font-bold px-4 py-2 hover:bg-white transition uppercase">Download .bin</a>
                <a href="https://espressif.github.io/esptool-js/" target="_blank" class="bg-[#f5a90f] text-black text-xs font-bold px-4 py-2 hover:bg-white transition uppercase">Web Flasher (Flash to 0x0)</a>
            </div>
        </div>

        <div class="mb-16 overflow-x-auto">"""
        
    with open('depin-hub/index.html', 'w') as f:
        f.write(pre + new_html + post)
    print("Success")
else:
    print("Markers not found")
