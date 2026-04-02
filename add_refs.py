import bs4
from bs4 import BeautifulSoup

with open('depin-hub/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Update UpRock link
for card in soup.find_all('div', class_='bg-card'):
    h4 = card.find('h4')
    if h4 and 'UpRock' in h4.text:
        a_tag = card.find('a', class_=lambda x: x and 'btn-visit' in x)
        if a_tag:
            a_tag['href'] = 'https://link.uprock.com/i/9be66bbc'
            a_tag.string = 'Join UpRock'
            a_tag['class'] = 'block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition mt-auto'.split()

# Find the "free" grid
free_section = soup.find('section', id='free')
grid = free_section.find('div', class_='grid')

# Add BlockGames, Farcaster, Zerion
new_html = """
    <!-- BlockGames -->
    <div class="bg-card p-6 rounded-xl hover:border-[#3fb950] transition duration-300">
        <div class="card-content">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <img src="https://logo.clearbit.com/blockgames.app" onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain=blockgames.app&sz=128';" alt="BlockGames Logo" class="project-logo mr-3 bg-white">
                    <h4 class="text-xl font-bold text-white">BlockGames</h4>
                </div>
                <span class="badge badge-android mt-1">App</span>
            </div>
            <p class="text-sm text-gray-400 mb-4">A cross-chain, universal player network. Play mobile games, build your player profile, and earn rewards and ecosystem airdrops.</p>
            <div class="flex flex-wrap gap-2 mb-4">
                <span class="badge badge-android">Android</span><span class="badge badge-browser">Browser</span>
            </div>
            <p class="text-xs text-[#58a6ff] mb-4">Yield: BLOCK / Points</p>
        </div>
        <a href="https://blockgames.app?referral_code=Micemeat" target="_blank" class="block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition mt-auto">Join BlockGames</a>
    </div>

    <!-- Farcaster -->
    <div class="bg-card p-6 rounded-xl hover:border-[#3fb950] transition duration-300">
        <div class="card-content">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <img src="https://logo.clearbit.com/farcaster.xyz" onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain=farcaster.xyz&sz=128';" alt="Farcaster Logo" class="project-logo mr-3 bg-white">
                    <h4 class="text-xl font-bold text-white">Farcaster</h4>
                </div>
                <span class="badge badge-android mt-1">Social</span>
            </div>
            <p class="text-sm text-gray-400 mb-4">A sufficiently decentralized social network (Warpcast app). Highly active community with frequent ecosystem airdrops for active users.</p>
            <div class="flex flex-wrap gap-2 mb-4">
                <span class="badge badge-android">Android</span><span class="badge badge-browser">Web</span>
            </div>
            <p class="text-xs text-[#58a6ff] mb-4">Yield: Ecosystem Airdrops</p>
        </div>
        <a href="https://farcaster.xyz/~/code/6LBJ0D" target="_blank" class="block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition mt-auto">Join Farcaster</a>
    </div>

    <!-- Zerion -->
    <div class="bg-card p-6 rounded-xl hover:border-[#3fb950] transition duration-300">
        <div class="card-content">
            <div class="flex justify-between items-start mb-4">
                <div class="flex items-center">
                    <img src="https://logo.clearbit.com/zerion.io" onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain=zerion.io&sz=128';" alt="Zerion Logo" class="project-logo mr-3 bg-white">
                    <h4 class="text-xl font-bold text-white">Zerion Wallet</h4>
                </div>
                <span class="badge badge-android mt-1">Wallet</span>
            </div>
            <p class="text-sm text-gray-400 mb-4">Smart Web3 wallet and portfolio tracker. Trade across networks, track your positions, and earn rewards and perks.</p>
            <div class="flex flex-wrap gap-2 mb-4">
                <span class="badge badge-android">Android</span><span class="badge badge-browser">Extension</span>
            </div>
            <p class="text-xs text-[#58a6ff] mb-4">Yield: Wallet Perks</p>
        </div>
        <a href="https://link.zerion.io/referral?code=BAGXB8864" target="_blank" class="block text-center bg-[#3fb950] text-black font-bold py-2 rounded-md hover:bg-[#2ea043] transition mt-auto">Get Zerion</a>
    </div>
"""

new_soup = BeautifulSoup(new_html, 'html.parser')
for child in new_soup.children:
    if isinstance(child, bs4.element.Tag):
        grid.append(child)

with open('depin-hub/index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
