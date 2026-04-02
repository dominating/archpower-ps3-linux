import re

with open('depin-hub/index.html', 'r') as f:
    content = f.read()

aro_html = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/aro.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            ARO Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Decentralized edge cloud infrastructure for AI and content delivery. Run a Lite Node to share bandwidth and earn passive rewards.">Decentralized edge cloud infrastructure for AI and content delivery. Run a Li...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">ARO Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://dashboard.aro.network/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join ARO</a>
                        </td>
                    </tr>"""

dawn_regex = re.compile(r'(<td class="px-4 py-4 text-right">\s*<a href="https://chromewebstore\.google\.com/detail/dawn[^>]+>Install Extension</a>\s*</td>\s*</tr>)', re.IGNORECASE)

if dawn_regex.search(content):
    content = dawn_regex.sub(r'\1' + aro_html, content)
    with open('depin-hub/index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Failed to find insertion point")
