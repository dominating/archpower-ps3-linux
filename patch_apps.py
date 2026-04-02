import re
with open("depin-hub/index.html", "r") as f:
    content = f.read()

# Helper function to add buttons
def add_buttons(content, project_name, play_store=None, app_store=None):
    # Find the row
    pattern = re.compile(r'(<td class="px-4 py-4 font-bold text-white flex items-center gap-3">\s*<img[^>]*>\s*)' + project_name, re.IGNORECASE)
    
    # Check if exists
    if not pattern.search(content):
        return content
        
    # Find the Platforms column for this row
    # The structure is: <td>Name</td> <td>Category</td> <td>Platforms</td>
    row_start = pattern.search(content).start()
    row_end = content.find("</tr>", row_start)
    row_content = content[row_start:row_end]
    
    # We want to insert badges in the Platforms column
    # Let's just find the third <td>
    tds = list(re.finditer(r'<td[^>]*>', row_content))
    if len(tds) >= 3:
        platforms_td_start = tds[2].end()
        platforms_td_end = row_content.find("</td>", platforms_td_start)
        
        platforms_content = row_content[platforms_td_start:platforms_td_end]
        
        new_badges = ""
        if play_store:
            new_badges += f' <a href="{play_store}" target="_blank" title="Google Play" class="inline-block"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Google_Play_Arrow_logo.svg" class="w-4 h-4 inline-block opacity-70 hover:opacity-100 transition"></a>'
        if app_store:
            new_badges += f' <a href="{app_store}" target="_blank" title="App Store" class="inline-block"><img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Apple_logo_white.svg" class="w-3.5 h-4 inline-block opacity-70 hover:opacity-100 transition ml-1"></a>'
            
        if new_badges:
            new_platforms_content = platforms_content.strip() + new_badges
            new_row_content = row_content[:platforms_td_start] + new_platforms_content + row_content[platforms_td_end:]
            content = content[:row_start] + new_row_content + content[row_end:]
            
    return content

# Add buttons
content = add_buttons(content, "DataHive AI", play_store="https://play.google.com/store/apps/details?id=ai.datahive.app")
content = add_buttons(content, "MyGate Network", play_store="https://play.google.com/store/apps/details?id=network.mygate.app")
content = add_buttons(content, "Silencio", play_store="https://play.google.com/store/apps/details?id=com.silencio", app_store="https://apps.apple.com/us/app/silencio/id1662990421")
content = add_buttons(content, "NodeGo AI", play_store="https://play.google.com/store/apps/details?id=ai.nodego.app")

with open("depin-hub/index.html", "w") as f:
    f.write(content)
print("Added app store buttons")
