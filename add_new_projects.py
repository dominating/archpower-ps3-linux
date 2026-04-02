import re

html_file = 'depin-hub/index.html'
with open(html_file, 'r') as f:
    html = f.read()

insert_pos = html.find('<tbody class="text-gray-300">')
if insert_pos == -1:
    print("Could not find tbody")
    exit(1)
    
insert_pos += len('<tbody class="text-gray-300">') + 1

new_rows = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/layeredge.io" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            LayerEdge
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Incentivized testnet for scalable compute on Bitcoin. Earn EDGE points by running a light node directly in your browser or VPS.">Incentivized testnet for scalable compute on Bitcoin. Earn EDGE points b...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser, VPS, Mobile</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">EDGE Points</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/layeredge-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/kaisar.io" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Kaisar Network (KAI)
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="DePIN on the peaq blockchain. Monetize idle GPU compute for the AI revolution via Checker Nodes.">DePIN on the peaq blockchain. Monetize idle GPU compute for the AI rev...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">PC, VPS, GPU Node</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">$KAI Airdrop</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/kaisar-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/openledger.net" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            OpenLedger
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Decentralized AI data infrastructure. Share bandwidth and data via extension to accumulate testnet points.">Decentralized AI data infrastructure. Share bandwidth and data via exten...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension, PC, VPS</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Testnet Points</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/openledger-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>
"""

html = html[:insert_pos] + new_rows + html[insert_pos:]

with open(html_file, 'w') as f:
    f.write(html)
print("Added projects to index.html")
