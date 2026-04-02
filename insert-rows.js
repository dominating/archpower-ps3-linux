const fs = require('fs');
const htmlFile = 'depin-hub/index.html';
let html = fs.readFileSync(htmlFile, 'utf8');

const newRows = `
                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <span class="w-6 h-6 rounded-sm bg-white/10 flex items-center justify-center text-xs">HN</span>
                            HedNet Protocol
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Decentralized bandwidth sharing and CPU/GPU compute sharing via Chrome Extension.">Decentralized bandwidth and compute via browser...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser Extension</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">HedNet Tokens</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/hednet.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <span class="w-6 h-6 rounded-sm bg-white/10 flex items-center justify-center text-xs">SLX</span>
                            Solix Network
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="AI-backed DePIN for sharing unused bandwidth to democratize internet infrastructure.">AI-backed DePIN for sharing unused bandwidth...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser / Node</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">Solix Rewards</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/solix.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>

                    <tr class="table-row-hover">
                        <td class="px-4 py-4 font-bold text-white flex items-center gap-3">
                            <span class="w-6 h-6 rounded-sm bg-white/10 flex items-center justify-center text-xs">DWN</span>
                            DAWN ($DAWN)
                        </td>
                        <td class="px-4 py-4 text-gray-400 whitespace-normal min-w-[250px] max-w-[400px] leading-snug" title="Solana DePIN turning bandwidth into blockchain rewards via the DAWN Validator Extension.">Solana DePIN turning bandwidth into rewards...</td>
                        <td class="px-4 py-4 text-xs font-mono text-gray-500">Browser Extension</td>
                        <td class="px-4 py-4 text-[#58a6ff] text-xs font-bold">$DAWN</td>
                        <td class="px-4 py-4 text-right">
                            <a href="/guides/dawn.md" target="_blank" class="inline-block bg-white/10 hover:bg-white/20 text-white text-xs px-3 py-1 ml-2 transition">Read Guide</a>
                        </td>
                    </tr>
`;

html = html.replace('<tbody class="text-gray-300">', '<tbody class="text-gray-300">\n' + newRows);
fs.writeFileSync(htmlFile, html);
console.log('Done inserting rows.');
