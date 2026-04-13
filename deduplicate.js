const fs = require('fs');
let html = fs.readFileSync('depin-hub/index.html', 'utf-8');

const tbodyRegex = /<tbody class="text-gray-300">([\s\S]*?)<\/tbody>/g;

html = html.replace(tbodyRegex, (match, p1) => {
    const rowRegex = /<tr class="table-row-hover">[\s\S]*?<\/tr>/g;
    let rows = [];
    let rMatch;
    
    while ((rMatch = rowRegex.exec(p1)) !== null) {
        rows.push(rMatch[0]);
    }
    
    let seen = new Set();
    let uniqueRows = [];
    
    for (let row of rows) {
        // extract text after the <img> tag in the first td
        const nameMatch = row.match(/<img[^>]*>\s*([^<]+)/);
        let name = nameMatch ? nameMatch[1].trim() : '';
        
        if (!name) {
            // fallback: just grab the text content of the first td
            const tdMatch = row.match(/<td[^>]*>([\s\S]*?)<\/td>/);
            if (tdMatch) {
                name = tdMatch[1].replace(/<[^>]*>/g, '').trim();
            }
        }
        
        // normalize name to catch minor differences (e.g., Kaisar Network vs Kaisar Network (KAI))
        let normalized = name.toLowerCase().replace(/[^a-z0-9]/g, '').replace('network', '').replace('zero', '').replace('kai', '');
        if(normalized.includes('kaisar')) normalized = 'kaisar'; // catch all kaisar
        
        if (!seen.has(normalized)) {
            seen.add(normalized);
            uniqueRows.push(row);
        } else {
            console.log('Removed duplicate:', name);
        }
    }
    
    return `<tbody class="text-gray-300">\n${uniqueRows.join('\n')}\n                    </tbody>`;
});

fs.writeFileSync('depin-hub/index.html', html);
console.log('Deduplication complete.');
