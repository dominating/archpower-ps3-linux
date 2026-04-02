from bs4 import BeautifulSoup

with open('depin-hub/index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the "free" grid (it's the first grid under section id="free")
free_section = soup.find('section', id='free')
grid = free_section.find('div', class_='grid')

# Create new Acurast card
acurast_html = """
                <div class="bg-card p-6 rounded-xl hover:border-[#3fb950] transition duration-300">
                    <div class="card-content">
                        <div class="flex justify-between items-start mb-4">
                            <div class="flex items-center">
                                <img src="https://logo.clearbit.com/acurast.com" onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain=acurast.com&sz=128';" alt="Acurast Logo" class="project-logo mr-3 bg-white">
                                <h4 class="text-xl font-bold text-white">Acurast</h4>
                            </div>
                            <span class="badge badge-android mt-1">Mobile App</span>
                        </div>
                        <p class="text-sm text-gray-400 mb-4">Turn your spare mobile device into a decentralized server. Mine and earn rewards by providing compute power via the Acurast app.</p>
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="badge badge-android">Android</span>
                        </div>
                        <p class="text-xs text-[#58a6ff] mb-4">Yield: cACU Tokens</p>
                    </div>
                    <a href="https://acurast.com/" target="_blank" class="block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition">Visit Website</a>
                </div>
"""

new_card = BeautifulSoup(acurast_html, 'html.parser').div
grid.append(new_card)

with open('depin-hub/index.html', 'w') as f:
    f.write(str(soup))
