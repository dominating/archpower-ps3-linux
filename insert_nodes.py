import re

with open('depin-hub/index.html', 'r') as f:
    content = f.read()

# We need to find the Browser Extensions table.
# We can look for the first <tbody> after "Browser Extensions"
extensions_tbody = content.find('<tbody>')
if extensions_tbody != -1:
    new_rows = """
                    <!-- Solix Network -->
                    <tr class="border-b border-gray-800 hover:bg-gray-800/30 transition group">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://www.google.com/s2/favicons?sz=128&domain=solix.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Solix Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Turn your unused bandwidth into SLIX rewards effortlessly with this DePIN extension.">Turn your unused bandwidth into SLIX rewards effortlessly with this DePIN extension.</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser Extension</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">$SLIX Rewards</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://solix.network" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join Solix</a>
                        </td>
                    </tr>
                    <!-- AIOZ Network -->
                    <tr class="border-b border-gray-800 hover:bg-gray-800/30 transition group">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://www.google.com/s2/favicons?sz=128&domain=aioz.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            AIOZ DePIN
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Provide storage, transcoding, and delivery services for media and earn $AIOZ.">Provide storage, transcoding, and delivery services for media and earn $AIOZ.</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Extension/Node</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">$AIOZ Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://aioz.network" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join AIOZ</a>
                        </td>
                    </tr>
"""
    # Find the end of the first tbody and insert there, or just at the beginning
    insert_pos = content.find('>', extensions_tbody) + 1
    content = content[:insert_pos] + new_rows + content[insert_pos:]

with open('depin-hub/index.html', 'w') as f:
    f.write(content)
