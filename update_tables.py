import re

with open('depin-hub/index.html', 'r') as f:
    content = f.read()

spark_row = """<tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://www.google.com/s2/favicons?sz=128&domain=sparkchain.ai" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            SparkChain
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Early-stage Solana DePIN extension that turns bandwidth into AI data.">Early-stage Solana DePIN extension that turns bandwidth into AI data.</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Spark Points</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://sparkchain.ai/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join Spark</a>
                        </td>
                    </tr>"""

rivalz_row = """<tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://www.google.com/s2/favicons?sz=128&domain=rivalz.ai" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Rivalz Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="AI data DePIN with an active desktop client (rClient) for node runners.">AI data DePIN with an active desktop client (rClient) for node runners.</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Desktop Node</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">RIZ Points</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://rivalz.ai/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join Rivalz</a>
                        </td>
                    </tr>"""

# Add Sparkchain to Browser Extensions (Table 1)
# Find the end of the first tbody
t1_match = re.search(r'(<h2[^>]*>1\. Browser Extensions.*?<tbody>.*?)(</tbody>)', content, re.DOTALL)
if t1_match:
    content = content[:t1_match.start(2)] + spark_row + "\n                    " + content[t1_match.start(2):]

# Add Rivalz to DePIN Nodes & Hardware (Table 3)
t3_match = re.search(r'(<h2[^>]*>3\. DePIN Nodes.*?<tbody>.*?)(</tbody>)', content, re.DOTALL)
if t3_match:
    content = content[:t3_match.start(2)] + rivalz_row + "\n                    " + content[t3_match.start(2):]

with open('depin-hub/index.html', 'w') as f:
    f.write(content)
