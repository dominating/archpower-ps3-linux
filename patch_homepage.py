import os

file_path = "jordan-homepage/index.html"
with open(file_path, "r") as f:
    html = f.read()

# Replace Name
html = html.replace("Jordan", "Micemeat")
html = html.replace("JORDAN", "MICEMEAT")

# Replace Footer links
html = html.replace('<a href="#" class="hover:text-white transition">GitHub</a>', '<a href="https://github.com/dominating" target="_blank" class="hover:text-white transition">GitHub</a>')
html = html.replace('<a href="#" class="hover:text-white transition">Twitter</a>', '<a href="https://x.com/micemeat" target="_blank" class="hover:text-white transition">X</a>')

with open(file_path, "w") as f:
    f.write(html)

print("Updated index.html")
