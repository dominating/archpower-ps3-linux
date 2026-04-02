html_path = 'depin-hub/index.html'
with open(html_path, 'r') as f:
    html = f.read()

unity_html = """
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <img src="https://logo.clearbit.com/unitynodes.io" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
                            Unity Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Turn your Android phone into an edge-computing telecom verification node, similar to Acurast.">Turn your Android phone into an edge-computing telecom verification nod...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Android App</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Unity Points</td>
                        <td class="px-4 py-4 text-right">
                            <a href="https://unitynodes.io/" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Join Unity</a>
                            <a href="/guides/unity-network.md" class="inline-block border border-[#58a6ff] text-[#58a6ff] text-xs font-bold px-3 py-1 ml-2 hover:bg-[#58a6ff] hover:text-black transition uppercase">View Guide</a>
                        </td>
                    </tr>
"""

parts = html.split('<tr class="table-row-hover">')
# Inject after the first occurrence or specific place. Let's just find UpRock and insert before it
if "UpRock" in html:
    up_idx = html.find("UpRock")
    tr_idx = html.rfind('<tr class="table-row-hover">', 0, up_idx)
    if tr_idx != -1:
        new_html = html[:tr_idx] + unity_html + html[tr_idx:]
        with open(html_path, 'w') as f:
            f.write(new_html)
        print("Patched.")
