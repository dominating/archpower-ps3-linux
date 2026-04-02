import re

with open('depin-hub/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert new rows into the "Software / Extensions (Free to Run)" table
new_rows = """
<tr>
    <td><span class="status-indicator active"></span>LayerEdge</td>
    <td>EVM Node</td>
    <td>Testnet / PC / VPS</td>
    <td>High</td>
    <td><a href="guides/layeredge-guide.md" class="guide-btn">View Guide</a></td>
</tr>
<tr>
    <td><span class="status-indicator active"></span>Kaisar Network</td>
    <td>AI/GPU Compute</td>
    <td>PC / VPS (peaq)</td>
    <td>High</td>
    <td><a href="guides/kaisar-guide.md" class="guide-btn">View Guide</a></td>
</tr>
<tr>
    <td><span class="status-indicator active"></span>OpenLedger</td>
    <td>AI Data Node</td>
    <td>Browser Extension</td>
    <td>Medium</td>
    <td><a href="guides/openledger-guide.md" class="guide-btn">View Guide</a></td>
</tr>
"""

if "<tbody>" in content:
    # Find the first tbody (which is Software / Extensions) and append rows
    content = content.replace("<tbody>", "<tbody>" + new_rows, 1)

with open('depin-hub/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
