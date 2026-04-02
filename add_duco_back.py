import re

with open('depin-hub/index.html', 'r') as f:
    content = f.read()

duco_html = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/duinocoin.com" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Duino-Coin (DUCO)
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Eco-friendly centralized cryptocurrency mining designed specifically for Arduino, ESP8266, ESP32 and Raspberry Pi.">Eco-friendly centralized cryptocurrency mining designed specifically fo...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">ESP32, Arduino, Pi</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">DUCO Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/duinocoin.md" class="inline-block border border-[#58a6ff] text-[#58a6ff] text-xs font-bold px-3 py-1 ml-2 hover:bg-[#58a6ff] hover:text-black transition uppercase">View Guide</a>
                        </td>
                    </tr>"""

grass_regex = re.compile(r'(<td class="px-4 py-4 text-right">\s*<a href="https://app\.grass\.io/register[^>]+>Join Grass</a>\s*</td>\s*</tr>)', re.IGNORECASE)

if grass_regex.search(content):
    content = grass_regex.sub(r'\1' + duco_html, content)
    with open('depin-hub/index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Failed to find insertion point")
