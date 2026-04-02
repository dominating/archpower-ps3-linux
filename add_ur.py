from bs4 import BeautifulSoup
import bs4

with open('depin-hub/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

free_section = soup.find('section', id='free')
grid = free_section.find('div', class_='grid')

ur_html = """
    <!-- Urnetwork -->
    <div class="bg-card p-6 rounded-xl hover:border-[#3fb950] transition duration-300">
        <div class="card-content">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <img src="https://logo.clearbit.com/ur.io" onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain=ur.io&sz=128';" alt="Urnetwork Logo" class="project-logo mr-3 bg-white">
                    <h4 class="text-xl font-bold text-white leading-tight">Urnetwork</h4>
                </div>
                <span class="badge badge-browser mt-1">Extension</span>
            </div>
            <p class="text-sm text-gray-400 mb-4">A decentralized AI infrastructure network. Share your bandwidth and computing power to earn daily rewards.</p>
            <div class="flex flex-wrap gap-2 mb-4">
                <span class="badge badge-windows">Windows</span><span class="badge badge-linux">Linux</span>
            </div>
            <p class="text-xs text-[#58a6ff] mb-4">Yield: Points</p>
        </div>
        <a href="https://ur.io/c?bonus=D39LIW" target="_blank" class="block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition mt-auto">Join Urnetwork</a>
    </div>
"""

new_node = BeautifulSoup(ur_html, 'html.parser')
for child in new_node.children:
    if isinstance(child, bs4.element.Tag):
        grid.append(child)

with open('depin-hub/index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
