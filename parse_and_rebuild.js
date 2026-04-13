const fs = require('fs');

const html = fs.readFileSync('depin-hub/index.html', 'utf-8');

// Extract the header / boilerplate
const headMatch = html.match(/([\s\S]*?)<!-- Featured Guide \(Hardcoded/);
let head = headMatch ? headMatch[1] : '';

// Create hardware-projects.html
const hardwareBoilerplate = head.replace('DePIN DIRECTORY', 'HARDWARE & HOMEBREW').replace('A minimalist, spreadsheet-friendly list...', 'Custom firmware, DIY hardware projects, and PS3 homebrew ports.');
const esp32Block = html.match(/<!-- Featured Guide \(Hardcoded[\s\S]*?<\/div>\s*<\/div>/)[0];
const ps3Block = html.match(/<!-- PS3 Homebrew \([\s\S]*?<\/div>\s*<\/div>/)[0];

const hardwareHtml = `${hardwareBoilerplate}
        ${esp32Block}
        ${ps3Block}
    </main>
</body>
</html>`;
fs.writeFileSync('depin-hub/hardware-projects.html', hardwareHtml);
console.log('Created hardware-projects.html');

// Now parse all table rows
const tableBodyMatch = html.match(/<tbody>([\s\S]*?)<\/tbody>/);
let rowsHtml = tableBodyMatch ? tableBodyMatch[1] : '';

if(!rowsHtml) {
    // maybe there's no tbody, just trs under thead. Let's extract everything between </thead> and </table>
    const fallbackMatch = html.match(/<\/thead>([\s\S]*?)<\/table>/);
    rowsHtml = fallbackMatch ? fallbackMatch[1] : '';
}

const rowRegex = /<tr class="table-row-hover">([\s\S]*?)<\/tr>/g;
let rows = [];
let match;
while ((match = rowRegex.exec(rowsHtml)) !== null) {
    const rowContent = match[0];
    // basic categorization logic
    let category = 'Unknown';
    if (rowContent.toLowerCase().includes('extension') || rowContent.toLowerCase().includes('browser')) {
        category = 'Extensions';
    } else if (rowContent.toLowerCase().includes('mobile') || rowContent.toLowerCase().includes('android') || rowContent.toLowerCase().includes('app')) {
        category = 'Apps';
    } else if (rowContent.toLowerCase().includes('node') || rowContent.toLowerCase().includes('vps') || rowContent.toLowerCase().includes('docker')) {
        category = 'Hardware & Nodes';
    } else {
        category = 'Other';
    }
    
    // Additional logic for specific apps that might overlap
    if (rowContent.toLowerCase().includes('extension') && rowContent.toLowerCase().includes('node')) {
        category = 'Extensions'; // prefer extension if it's a browser node
    }
    
    rows.push({ html: rowContent, category });
}

console.log(`Found ${rows.length} rows.`);

const grouped = {
    'Extensions': rows.filter(r => r.category === 'Extensions').map(r => r.html).join('\n'),
    'Bandwidth & Mobile Apps': rows.filter(r => r.category === 'Apps').map(r => r.html).join('\n'),
    'DePIN Nodes & Hardware': rows.filter(r => r.category === 'Hardware & Nodes' || r.category === 'Other').map(r => r.html).join('\n')
};

// Now rebuild index.html without the hardware blocks, but with new tables
const giveawaysBlockMatch = html.match(/<!-- LIVE GIVEAWAYS WIDGET -->[\s\S]*?<!-- GIVEAWAYS_END -->\s*<\/div>\s*<\/div>/);
const giveawaysBlock = giveawaysBlockMatch ? giveawaysBlockMatch[0] : '';

function makeTable(title, borderClass, rowsHtml) {
    if (!rowsHtml.trim()) return '';
    return `
        <div class="mb-16 overflow-x-auto">
            <h2 class="text-2xl font-bold uppercase tracking-tighter mb-4 text-white border-l-4 ${borderClass} pl-3">${title}</h2>
            <div class="bg-[#111] border border-gray-800 rounded-sm">
                <table class="w-full text-left text-sm whitespace-nowrap">
                    <thead>
                        <tr class="bg-[#0a0a0a]">
                            <th class="px-4 py-4">Project</th>
                            <th class="px-4 py-4">Description</th>
                            <th class="px-4 py-4">Platforms</th>
                            <th class="px-4 py-4">Yield / Reward</th>
                            <th class="px-4 py-4 text-right">Action</th>
                        </tr>
                    </thead>
                    <tbody class="text-gray-300">
                        ${rowsHtml}
                    </tbody>
                </table>
            </div>
        </div>
    `;
}

// Add our newly added guides (Chakra, Depinsim, Interlink) manually if they aren't parsed
const newGuidesHtml = `
<tr class="table-row-hover">
    <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
        <img src="https://logo.clearbit.com/chakranetwork.io" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
        Chakra Network
    </td>
    <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="AI-optimized data mapping using unused bandwidth on Solana.">AI-optimized data mapping using unused bandwidth on Solana...</td>
    <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser (Extension)</td>
    <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Chakra Points</td>
    <td class="px-4 py-4 text-right">
        <a href="/guides/chakra-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
    </td>
</tr>
<tr class="table-row-hover">
    <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
        <img src="https://logo.clearbit.com/depinsim.com" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
        Depinsim (ESIM)
    </td>
    <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Decentralized telecom frontier network and eSIM.">Decentralized telecom frontier network and eSIM...</td>
    <td class="px-4 py-4 text-xs font-mono text-gray-500">Mobile (eSIM)</td>
    <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">ESIM Tokens</td>
    <td class="px-4 py-4 text-right">
        <a href="/guides/depinsim-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
    </td>
</tr>
<tr class="table-row-hover">
    <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
        <img src="https://logo.clearbit.com/interlink.network" class="w-6 h-6 rounded-sm bg-white p-0.5" onerror="this.style.display='none'">
        Interlink (ITLG)
    </td>
    <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Dual-token real-world utility DePIN.">Dual-token real-world utility DePIN...</td>
    <td class="px-4 py-4 text-xs font-mono text-gray-500">PC, VPS, Linux</td>
    <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">ITLG Tokens</td>
    <td class="px-4 py-4 text-right">
        <a href="/guides/interlink-guide.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
    </td>
</tr>
`;

grouped['Extensions'] = newGuidesHtml.match(/Chakra/i) ? grouped['Extensions'] : newGuidesHtml + grouped['Extensions'];

// Rebuild nav to include a link to hardware projects
let finalHead = head.replace(
    /<a href="https:\/\/cryptol\.ink\/pFRkJO" class="text-\[#58a6ff\] hover:text-white transition">Miceprogramming Hub ↗<\/a>/,
    `<a href="/hardware-projects.html" class="text-white hover:text-[#58a6ff] transition mr-6">Hardware & Homebrew</a>
            <a href="https://cryptol.ink/pFRkJO" class="text-[#58a6ff] hover:text-white transition">Miceprogramming Hub ↗</a>`
);

let newIndex = `${finalHead}
        ${giveawaysBlock}

        <div class="mb-8 p-4 bg-blue-900/20 border border-blue-500/30 rounded-md text-blue-200 text-sm">
            <strong>Update:</strong> Custom ESP32 Firmware and PS3 Homebrew ports have been moved to the <a href="/hardware-projects.html" class="underline text-[#58a6ff] hover:text-white">Hardware & Homebrew section</a>.
        </div>

        ${makeTable('1. Browser Extensions', 'border-[#58a6ff]', grouped['Extensions'])}
        ${makeTable('2. Mobile & Bandwidth Apps', 'border-green-500', grouped['Bandwidth & Mobile Apps'])}
        ${makeTable('3. DePIN Nodes & Hardware', 'border-purple-500', grouped['DePIN Nodes & Hardware'])}

    </main>
</body>
</html>`;

fs.writeFileSync('depin-hub/index.html', newIndex);
console.log('Successfully rebuilt index.html');
