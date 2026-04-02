import re

with open("depin-hub/index.html", "r") as f:
    html = f.read()

# Replace the "Join Titan Network" button with a two-button flex layout or just replace it.
titan_old_btn = '<a class="block text-center text-white font-bold py-2 rounded-md transition mt-auto hover:opacity-80" href="https://test1.titannet.io/intiveRegister?code=tbXASf" style="background-color: #0ea5e9;" target="_blank">Join Titan Network</a>'
titan_new_btns = """<div class="mt-auto flex gap-2">
<a class="flex-1 text-center text-sm font-bold py-2 rounded-md transition hover:opacity-80 bg-gray-700 text-white" href="/guides/titan-network-guide.md" target="_blank">Guide</a>
<a class="flex-1 text-center text-sm font-bold py-2 rounded-md transition hover:opacity-80 text-white" href="https://test1.titannet.io/intiveRegister?code=tbXASf" style="background-color: #0ea5e9;" target="_blank">Join</a>
</div>"""

html = html.replace(titan_old_btn, titan_new_btns)

with open("depin-hub/index.html", "w") as f:
    f.write(html)
print("Patched Titan Network.")
