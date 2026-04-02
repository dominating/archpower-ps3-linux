import re

with open("depin-hub/index.html", "r") as f:
    html = f.read()

# Check if giveaway section exists
if '<!-- GIVEAWAYS_START -->' in html:
    # Inject some hardcoded giveaways since X scraper isn't working
    giveaways = [
        {
            "author": "Power Mining & Tech Hustler",
            "text": "Giving away one of the most popular and powerful Solo Bitcoin Miners 🔥 NerdQAxe++ 4.8TH (Value $500). Multiple ways to enter!",
            "link": "https://sweepsmadness.com/giveaways/bitcoin-miner-giveaway/"
        },
        {
            "author": "Funky Kit Show",
            "text": "LIVE Ep.371 - Gigabyte X870E AORUS PRO X3D ICE, Watercooled Bitaxe GT 800, Prize Giveaway. Watch our stream and enter to win!",
            "link": "https://www.funkykit.com/fktv-vlogs/the-funky-kit-show-live-ep-371-gigabyte-x870e-aorus-pro-x3d-ice-watercooled-bitaxe-gt-800-prize-giveaway"
        },
        {
            "author": "BlockChance",
            "text": "Win a Bitcoin currently valued at $95,390 with our BlockChance™ Bitcoin Ticket Miner! Or win a new ASIC. Enter via mail-in or purchase.",
            "link": "https://sweepstakesfanatics.com/coinbase-march-giveaway-purchase-mail-in/"
        }
    ]
    
    html_blocks = []
    for g in giveaways:
        html_blocks.append(f'''
                <!-- GIVEAWAY ITEM -->
                <div class="p-4 bg-[#161b22] border border-gray-800 rounded-md hover:border-[#58a6ff] transition group flex flex-col justify-between min-h-[140px]">
                    <div>
                        <p class="text-sm font-bold text-white mb-2 truncate" title="{g['author']}">{g['author']}</p>
                        <p class="text-xs text-gray-400 mb-4 line-clamp-3">{g['text']}</p>
                    </div>
                    <a href="{g['link']}" target="_blank" class="mt-auto text-xs font-mono text-[#58a6ff] hover:text-white transition group-hover:underline">Enter Giveaway →</a>
                </div>''')

    combined_html = "\n".join(html_blocks)
    
    # Replace existing giveaways
    pattern = re.compile(r'(<!-- GIVEAWAYS_START -->)(.*?)(<!-- GIVEAWAYS_END -->)', re.DOTALL)
    new_html = html[:pattern.search(html).start(2)] + '\n' + combined_html + '\n                ' + html[pattern.search(html).end(2):]
    
    with open("depin-hub/index.html", "w") as f:
        f.write(new_html)
    print("Updated giveaways in index.html")
else:
    # Add a giveaway section if it doesn't exist
    print("GIVEAWAYS_START not found, let's add it.")
    
    giveaways_section = """
        <div class="w-full max-w-5xl mt-12 mb-8 px-4">
            <h2 class="text-2xl font-bold mb-6 text-white jp-text border-b border-gray-800 pb-2">HARDWARE GIVEAWAYS // LIVE</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <!-- GIVEAWAYS_START -->
                <!-- GIVEAWAY ITEM -->
                <div class="p-4 bg-[#161b22] border border-gray-800 rounded-md hover:border-[#58a6ff] transition group flex flex-col justify-between min-h-[140px]">
                    <div>
                        <p class="text-sm font-bold text-white mb-2 truncate" title="Power Mining & Tech Hustler">Power Mining & Tech Hustler</p>
                        <p class="text-xs text-gray-400 mb-4 line-clamp-3">Giving away one of the most popular and powerful Solo Bitcoin Miners 🔥 NerdQAxe++ 4.8TH (Value $500). Multiple ways to enter!</p>
                    </div>
                    <a href="https://sweepsmadness.com/giveaways/bitcoin-miner-giveaway/" target="_blank" class="mt-auto text-xs font-mono text-[#58a6ff] hover:text-white transition group-hover:underline">Enter Giveaway →</a>
                </div>
                <!-- GIVEAWAY ITEM -->
                <div class="p-4 bg-[#161b22] border border-gray-800 rounded-md hover:border-[#58a6ff] transition group flex flex-col justify-between min-h-[140px]">
                    <div>
                        <p class="text-sm font-bold text-white mb-2 truncate" title="Funky Kit Show">Funky Kit Show</p>
                        <p class="text-xs text-gray-400 mb-4 line-clamp-3">LIVE Ep.371 - Gigabyte X870E AORUS PRO X3D ICE, Watercooled Bitaxe GT 800, Prize Giveaway. Watch our stream and enter to win!</p>
                    </div>
                    <a href="https://www.funkykit.com/fktv-vlogs/the-funky-kit-show-live-ep-371-gigabyte-x870e-aorus-pro-x3d-ice-watercooled-bitaxe-gt-800-prize-giveaway" target="_blank" class="mt-auto text-xs font-mono text-[#58a6ff] hover:text-white transition group-hover:underline">Enter Giveaway →</a>
                </div>
                <!-- GIVEAWAY ITEM -->
                <div class="p-4 bg-[#161b22] border border-gray-800 rounded-md hover:border-[#58a6ff] transition group flex flex-col justify-between min-h-[140px]">
                    <div>
                        <p class="text-sm font-bold text-white mb-2 truncate" title="BlockChance">BlockChance</p>
                        <p class="text-xs text-gray-400 mb-4 line-clamp-3">Win a Bitcoin currently valued at $95,390 with our BlockChance™ Bitcoin Ticket Miner! Or win a new ASIC. Enter via mail-in or purchase.</p>
                    </div>
                    <a href="https://sweepstakesfanatics.com/coinbase-march-giveaway-purchase-mail-in/" target="_blank" class="mt-auto text-xs font-mono text-[#58a6ff] hover:text-white transition group-hover:underline">Enter Giveaway →</a>
                </div>
                <!-- GIVEAWAYS_END -->
            </div>
        </div>
"""

    # Insert before the table
    if '<div class="w-full max-w-5xl overflow-x-auto bg-[#0a0a0a] rounded-lg border border-[#1a1a1a] shadow-2xl">' in html:
        parts = html.split('<div class="w-full max-w-5xl overflow-x-auto bg-[#0a0a0a] rounded-lg border border-[#1a1a1a] shadow-2xl">')
        new_html = parts[0] + giveaways_section + '<div class="w-full max-w-5xl overflow-x-auto bg-[#0a0a0a] rounded-lg border border-[#1a1a1a] shadow-2xl">' + parts[1]
        with open("depin-hub/index.html", "w") as f:
            f.write(new_html)
        print("Inserted new giveaways section")
    else:
        print("Couldn't find insertion point")
