import re

with open('depin-hub/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

additions = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/gradient.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Gradient Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="DePIN focused on reducing AI training costs via lightweight Sentry Nodes.">DePIN focused on reducing AI training costs via lightweight Sentry Nodes...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension, Web</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Points / Airdrop</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://gradient.network/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join Gradient</a>
                        </td>
                    </tr>
                    
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/kaichain.net" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            KAI Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="KAI sits at the intersection of GPUs, AI, and DePIN. Testnet/mainnet nodes available.">KAI sits at the intersection of GPUs, AI, and DePIN. Testnet/mainnet no...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Linux, Windows</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">KAI Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://kai.network/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Visit KAI</a>
                        </td>
                    </tr>
"""

# inject right before the closing </tbody> of the first table
html = html.replace('</tbody>', additions + '\n                </tbody>', 1)

with open('depin-hub/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
