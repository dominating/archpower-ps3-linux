from bs4 import BeautifulSoup

with open('depin-hub/index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all grids
grids = soup.find_all('div', class_='grid')

for grid in grids:
    seen_titles = set()
    cards = grid.find_all('div', class_='bg-card', recursive=False)
    for card in cards:
        title_tag = card.find('h4')
        if title_tag:
            title = title_tag.get_text(strip=True)
            if title in seen_titles:
                # remove the card
                card.decompose()
            else:
                seen_titles.add(title)

with open('depin-hub/index.html', 'w') as f:
    f.write(str(soup))
