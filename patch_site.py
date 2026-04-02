import bs4
from bs4 import BeautifulSoup

with open('depin-hub/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

free_section = soup.find('section', id='free')
grid = free_section.find('div', class_='grid')

teneo_html = """
    <!-- Teneo -->
    <div class="bg-card p-6 rounded-xl hover:border-[#3fb950] transition duration-300">
        <div class="card-content">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <img src="https://logo.clearbit.com/teneo.pro" onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain=teneo.pro&sz=128';" alt="Teneo Logo" class="project-logo mr-3 bg-white">
                    <h4 class="text-xl font-bold text-white leading-tight">Teneo</h4>
                </div>
                <span class="badge badge-browser mt-1">Extension</span>
            </div>
            <p class="text-sm text-gray-400 mb-4">Earn rewards by running a community node and sharing your unused bandwidth.</p>
            <div class="flex flex-wrap gap-2 mb-4">
                <span class="badge badge-windows">Windows</span><span class="badge badge-linux">Linux</span>
            </div>
            <p class="text-xs text-[#58a6ff] mb-4">Yield: Teneo Points</p>
        </div>
        <div class="flex flex-col gap-2 mt-auto">
            <a href="https://dashboard.teneo.pro/auth/signup?referralCode=jX9Hu" target="_blank" class="block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition">Join Teneo</a>
        </div>
    </div>
"""

# Insert Teneo
new_node = BeautifulSoup(teneo_html, 'html.parser')
for child in new_node.children:
    if isinstance(child, bs4.element.Tag):
        grid.append(child)

# Update Dawn Link
dawn_link = soup.find('a', href="https://www.dawninternet.com/")
if dawn_link:
    dawn_link['href'] = "https://chromewebstore.google.com/detail/dawn-validator-chrome-ext/fpdkjdnhkakefebpekbdhillbhonfjjp"
    dawn_link.string = "Install Extension"
    # Change class to the green button style instead of outline
    dawn_link['class'] = "block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition mb-2".split()

with open('depin-hub/index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
