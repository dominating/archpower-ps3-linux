import re
from bs4 import BeautifulSoup

with open("depin-hub/index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

categories = []

for section in soup.find_all('section'):
    h3 = section.find('h3')
    if not h3:
        continue
    cat_name = h3.get_text(strip=True)
    cards = []
    
    for card in section.find_all('div', class_='bg-card'):
        img = card.find('img')
        logo_url = img['src'] if img else ''
        name_tag = card.find('h4')
        name = name_tag.get_text(separator=" ", strip=True) if name_tag else "Unknown"
        
        desc_tag = card.find('p', class_=re.compile("text-sm"))
        desc = desc_tag.get_text(strip=True) if desc_tag else ""
        
        badges = []
        for badge in card.find_all('span', class_=re.compile("badge")):
            b_text = badge.get_text(strip=True)
            if b_text and b_text not in badges:
                badges.append(b_text)
                
        yield_tag = card.find('p', class_=re.compile("text-xs.*mb-4"))
        yield_text = yield_tag.get_text(strip=True).replace("Yield: ", "").replace("Investment: ", "") if yield_tag else ""
        
        links = []
        for a in card.find_all('a'):
            links.append({"href": a['href'], "text": a.get_text(strip=True)})
            
        ref_tag = card.find('p', text=re.compile("Ref Code:"))
        ref_code = ""
        if ref_tag:
            span = ref_tag.find('span')
            if span:
                ref_code = span.get_text(strip=True)
                
        cards.append({
            "name": name,
            "logo": logo_url,
            "desc": desc,
            "badges": ", ".join(badges),
            "yield": yield_text,
            "links": links,
            "ref_code": ref_code
        })
        
    categories.append({
        "name": cat_name,
        "cards": cards
    })

# Now let's build the new HTML
new_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PassivePin | DePIN & Airdrop Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=Noto+Sans+JP:wght@300;400;700&display=swap');
        
        body {
            background-color: #050505;
            color: #e2e8f0;
            font-family: 'Space Grotesk', sans-serif;
            overflow-x: hidden;
        }

        .bg-grid {
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(255, 255, 255, 0.05) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
            mask-image: linear-gradient(to bottom, transparent, black, transparent);
            -webkit-mask-image: linear-gradient(to bottom, transparent 10%, black 50%, transparent 90%);
        }

        .jp-text {
            font-family: 'Noto Sans JP', sans-serif;
            color: #58a6ff;
            opacity: 0.8;
            letter-spacing: 0.2em;
        }

        .glitch-text {
            position: relative;
            color: white;
        }

        .glitch-text::before, .glitch-text::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.8;
        }

        .glitch-text::before {
            left: 2px;
            text-shadow: -2px 0 #ff00c1;
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim 5s infinite linear alternate-reverse;
        }

        .glitch-text::after {
            left: -2px;
            text-shadow: -2px 0 #00fff9, 2px 2px #ff00c1;
            animation: glitch-anim2 5s infinite linear alternate-reverse;
        }

        @keyframes glitch-anim {
            0% { clip: rect(21px, 9999px, 8px, 0); }
            20% { clip: rect(72px, 9999px, 92px, 0); }
            40% { clip: rect(10px, 9999px, 43px, 0); }
            60% { clip: rect(88px, 9999px, 12px, 0); }
            80% { clip: rect(31px, 9999px, 66px, 0); }
            100% { clip: rect(54px, 9999px, 23px, 0); }
        }

        @keyframes glitch-anim2 {
            0% { clip: rect(65px, 9999px, 100px, 0); }
            20% { clip: rect(2px, 9999px, 24px, 0); }
            40% { clip: rect(89px, 9999px, 55px, 0); }
            60% { clip: rect(12px, 9999px, 88px, 0); }
            80% { clip: rect(43px, 9999px, 10px, 0); }
            100% { clip: rect(92px, 9999px, 72px, 0); }
        }

        .table-row-hover:hover {
            background-color: rgba(255, 255, 255, 0.03);
        }
        
        table {
            border-collapse: collapse;
        }
        
        th {
            border-bottom: 1px solid #333;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.1em;
            color: #888;
        }
        
        td {
            border-bottom: 1px solid #1a1a1a;
        }
    </style>
</head>
<body class="relative min-h-screen flex flex-col items-center">
    
    <!-- Background Grid -->
    <div class="fixed inset-0 w-full h-full bg-grid z-0 pointer-events-none"></div>

    <!-- Navigation -->
    <nav class="w-full max-w-7xl mx-auto px-6 py-8 relative z-10 flex justify-between items-center">
        <div class="text-2xl font-bold tracking-tighter">PASSIVEPIN<span class="text-[#58a6ff]">.</span></div>
        <div class="flex space-x-6 text-sm font-semibold tracking-widest uppercase">
            <a href="https://jordan-homepage-sigma.vercel.app" class="text-[#58a6ff] hover:text-white transition">Jordan's Hub ↗</a>
        </div>
    </nav>

    <!-- Hero Section -->
    <main class="w-full max-w-7xl mx-auto px-6 py-12 relative z-10 flex flex-col flex-grow">
        
        <div class="mb-12">
            <span class="jp-text text-sm font-bold block mb-2">分散型物理インフラネットワーク</span>
            <h1 class="text-4xl md:text-6xl font-black mb-4 uppercase tracking-tighter" data-text="DePIN DIRECTORY">
                <span class="glitch-text" data-text="DePIN DIRECTORY">DePIN DIRECTORY</span>
            </h1>
            <p class="text-lg text-gray-400 max-w-2xl leading-relaxed">
                A minimalist, spreadsheet-friendly list of active DePIN nodes, extensions, and passive yield opportunities. Select, copy, and paste straight to Excel.
            </p>
        </div>

        <!-- Featured Guide (Hardcoded for DuinoCoin) -->
        <div class="w-full bg-[#111] border border-[#58a6ff]/30 p-6 mb-16 rounded-sm">
            <h3 class="text-xl font-bold text-[#58a6ff] uppercase tracking-widest mb-2">Featured: Headless Duino Miner</h3>
            <p class="text-gray-400 text-sm mb-4">Compiled C++ firmware for the ESP32-S2 USB Dongle. Stripped of monitor dependencies for silent, ultra-efficient DuinoCoin hashing.</p>
            <div class="flex items-center gap-4">
                <a href="/firmware/s2/duco/merged.bin" class="bg-[#58a6ff] text-black text-xs font-bold px-4 py-2 hover:bg-white transition uppercase">Download .bin</a>
                <code class="text-xs text-[#f5a90f] bg-black px-3 py-2 border border-gray-800">esptool.py -p /dev/ttyACM0 -b 460800 write_flash 0x0 merged.bin</code>
            </div>
        </div>

"""

for cat in categories:
    if not cat['cards']: continue
    new_html += f"""
        <div class="mb-16 overflow-x-auto">
            <h2 class="text-2xl font-bold uppercase tracking-tighter mb-4 text-white border-l-4 border-[#58a6ff] pl-3">{cat['name']}</h2>
            <table class="w-full text-left text-sm whitespace-nowrap">
                <thead>
                    <tr>
                        <th class="px-4 py-4">Project</th>
                        <th class="px-4 py-4">Description</th>
                        <th class="px-4 py-4">Platforms</th>
                        <th class="px-4 py-4">Yield / Reward</th>
                        <th class="px-4 py-4 text-right">Action</th>
                    </tr>
                </thead>
                <tbody class="text-gray-300">
"""
    for card in cat['cards']:
        links_html = ""
        for link in card['links']:
            # Make buttons minimal
            links_html += f'<a href="{link["href"]}" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">{link["text"]}</a>'
            
        ref_html = f'<div class="text-[10px] text-gray-500 mt-1">Ref: {card["ref_code"]}</div>' if card["ref_code"] else ''
        
        desc_short = card["desc"]
        if len(desc_short) > 75:
            desc_short = desc_short[:72] + "..."
            
        new_html += f"""
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="{card['logo']}" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            {card['name']}
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="{card['desc']}">{desc_short}</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">{card['badges']}</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">{card['yield']}</td>
                        <td class="px-4 py-4 text-right">
                            {links_html}
                            {ref_html}
                        </td>
                    </tr>
"""
    new_html += """
                </tbody>
            </table>
        </div>
"""

new_html += """
    </main>

    <!-- Footer -->
    <footer class="w-full border-t border-gray-900 bg-[#050505] relative z-10 py-8 mt-auto">
        <div class="max-w-7xl mx-auto px-6 flex justify-between items-center text-sm text-gray-600 font-mono">
            <div>&copy; 2026 PASSIVEPIN. Auto-updating DePIN hub.</div>
            <div class="flex space-x-4">
                <a href="https://jordan-homepage-sigma.vercel.app" class="hover:text-white transition">About the Creator</a>
            </div>
        </div>
    </footer>

</body>
</html>
"""

with open("depin-hub/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Rebuilt index.html with new theme and table layout.")
