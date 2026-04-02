import re

with open('depin-hub/index.html', 'r') as f:
    content = f.read()

nano_html = """
        <div class="w-full bg-[#111] border border-[#58a6ff]/30 p-6 mb-16 rounded-sm">
            <h3 class="text-xl font-bold text-[#58a6ff] uppercase tracking-widest mb-2">Featured: ESP32-S2 Nano (XNO) Auto-Exchange Miner</h3>
            <p class="text-gray-400 text-sm mb-4">Optimized NM-TV/NerdMiner V2 firmware for the ZY ESP32-S2 USB Dongle (240MHz + Thermal Throttling @ 75°C). Configured for low-power SHA256 mining with direct payouts in Nano (XNO) via Unmineable-style pools.</p>
            <div class="flex items-center gap-4">
                <a href="/guides/nerdminer-nano.md" class="border border-[#58a6ff] text-[#58a6ff] text-xs font-bold px-4 py-2 hover:bg-[#58a6ff] hover:text-black transition uppercase">View Guide</a>
                <a href="/firmware/s2/nerdminer-dgb-merged.bin" class="bg-[#58a6ff] text-black text-xs font-bold px-4 py-2 hover:bg-white transition uppercase">Download .bin</a>
            </div>
        </div>
"""

dgb_regex = re.compile(r'(<h3 class="text-xl font-bold text-\[\#58a6ff\] uppercase tracking-widest mb-2">Featured: ESP32-S2 Digibyte Miner \(NerdMiner V2\)</h3>.*?</div>\s*</div>)', re.IGNORECASE | re.DOTALL)

if dgb_regex.search(content):
    content = dgb_regex.sub(r'\1' + nano_html, content)
    with open('depin-hub/index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Failed to find insertion point")
