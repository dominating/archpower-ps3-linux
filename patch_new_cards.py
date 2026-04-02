import re

html_path = 'depin-hub/index.html'
with open(html_path, 'r') as f:
    html = f.read()

new_rows = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/layeredge.io" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            LayerEdge
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Incentivized EVM testnet for Bitcoin-backed compute via a light node.">Incentivized EVM testnet for Bitcoin-backed compute via a light node...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser (Extension)</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">EDGE Points -> Airdrop</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/layeredge-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/kaisar.io" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Kaisar Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Decentralized AI and compute DePIN on the peaq blockchain. Earn from idle GPUs.">Decentralized AI and compute DePIN on the peaq blockchain...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">PC, VPS, GPU</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">KAI Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/kaisar-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/openledger.net" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            OpenLedger
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Decentralized AI data infrastructure with exclusive datanet airdrops.">Decentralized AI data infrastructure with exclusive datanet airdrops...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser Extension</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Testnet Points</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/openledger-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>
"""

# Insert right after the <tbody> of the "Zero Investment" table
if '<table' in html:
    # Find the second table or the one after Zero Investment
    # Just insert right after <thead> -> </tr> -> </thead> -> \n (or <tbody> if present)
    html = re.sub(r'(</thead>\s*)', r'\1' + new_rows, html, count=1)
    with open(html_path, 'w') as f:
        f.write(html)
    print("Added new rows successfully.")
else:
    print("Could not find table in index.html")
