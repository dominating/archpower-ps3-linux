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
        const nameMatch = row.match(/<img[^>]*>\s*([^<\n]+)/);
        let name = nameMatch ? nameMatch[1].trim() : '';
        
        if (!name) {
            const tdMatch = row.match(/<td[^>]*>([\s\S]*?)<\/td>/);
            if (tdMatch) name = tdMatch[1].replace(/<[^>]*>/g, '').trim();
        }
        
        let baseName = name.toLowerCase().replace(/[^a-z]/g, '');
        if(baseName.includes('kaisar')) baseName = 'kaisar';
        if(baseName.includes('gradient')) baseName = 'gradient';
        if(baseName.includes('dawn')) baseName = 'dawn';
        if(baseName.includes('layeredge')) baseName = 'layeredge';
        if(baseName.includes('openledger')) baseName = 'openledger';
        
        if (!seen.has(baseName)) {
            seen.add(baseName);
            uniqueRows.push(row);
        } else {
            console.log('Removed duplicate again:', name);
        }
    }
    
    return `<tbody class="text-gray-300">\n${uniqueRows.join('\n')}\n                    </tbody>`;
});

fs.writeFileSync('depin-hub/index.html', html);
console.log('Deduplication 2 complete.');
