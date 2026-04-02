import re

with open("depin-hub/index.html", "r") as f:
    html = f.read()

# Replace the specific video block
video_block_pattern = r'<div class="w-full md:w-1/2 rounded-xl overflow-hidden border border-\[\#30363d\] shadow-lg relative aspect-\[16/9\] bg-black flex items-center justify-center">.*?</div>'
html = re.sub(video_block_pattern, '', html, flags=re.DOTALL)

# Update the left column to be full width, or wider
html = html.replace('<div class="w-full md:w-1/2">\n            <h3 class="text-3xl', '<div class="w-full md:w-2/3 mx-auto">\n            <h3 class="text-3xl')

with open("depin-hub/index.html", "w") as f:
    f.write(html)

print("Patch applied.")
