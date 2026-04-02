import re

html_path = 'depin-hub/index.html'
with open(html_path, 'r') as f:
    html = f.read()

giveaways_html = """
        <!-- LIVE GIVEAWAYS WIDGET -->
        <div class="mb-10 bg-[#0d1117] border border-gray-800 rounded-lg p-6 shadow-lg shadow-black/50">
            <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2 border-l-4 border-yellow-500 pl-3">
                <span class="">🎁</span> Live Crypto & DePIN Giveaways
                <span class="text-xs font-normal text-gray-400 ml-auto flex items-center gap-1">
                    <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span> Auto-updating
                </span>
            </h2>
            <div id="giveaways-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
<!-- GIVEAWAYS_START -->
                <div class="p-4 bg-[#161b22] border border-gray-800 rounded-md flex flex-col items-center justify-center text-center text-gray-500 min-h-[120px]">
                    <p class="text-sm">Awaiting X.com bot initialization...</p>
                    <p class="text-xs mt-1 text-[#58a6ff]">Check back tomorrow!</p>
                </div>
<!-- GIVEAWAYS_END -->
            </div>
        </div>
"""

new_html = html.replace('<div class="mb-16 overflow-x-auto">', giveaways_html + '\n        <div class="mb-16 overflow-x-auto">')
with open(html_path, 'w') as f:
    f.write(new_html)
print("Successfully injected Giveaways UI into index.html")
