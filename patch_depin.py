import os

html_to_add = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/mygate.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            MyGate Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="DePIN project on Solana that turns personal devices into VPS servers by monetizing unused bandwidth. Backed by Solana Foundation & Multicoin Capital.">DePIN project on Solana that turns personal devices into VPS servers by monet...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension/Node</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">$MYG Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://app.mygate.network/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join MyGate</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/deepnode.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            DeepNode
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Emerging DePIN protocol for distributed infrastructure with an early access points program for the confirmed $DN token airdrop.">Emerging DePIN protocol for distributed infrastructure with an early access p...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension/Node</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">$DN Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://x.com/DeepNode_DePIN" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join DeepNode</a>
                        </td>
                    </tr>
"""

path = '/home/micemeat/.openclaw/workspace/depin-hub/index.html'
with open(path, 'r') as f:
    content = f.read()

content = content.replace('<tbody class="text-gray-300">', '<tbody class="text-gray-300">\n' + html_to_add)

with open(path, 'w') as f:
    f.write(content)
