const fs = require('fs');
const path = require('path');
const https = require('https');

const userId = "user_micebot_api";
const apiUrl = "https://cryptol.ink/api/create";

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function shortenUrl(url) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({ url, userId });
    const req = https.request(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        'Content-Length': data.length
      }
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', async () => {
        try {
          const json = JSON.parse(body);
          if (json.success && json.shortUrl) {
            resolve(json.shortUrl);
          } else if (json.code === 'RATE_LIMITED') {
            const waitTime = (json.retry_after || 62) * 1000;
            console.log(`Rate limited on ${url}. Waiting ${waitTime/1000} seconds...`);
            await sleep(waitTime + 1000);
            resolve(await shortenUrl(url)); // retry
          } else {
            console.error('Failed to shorten:', url, json);
            resolve(url);
          }
        } catch (e) {
          console.error('Error parsing JSON for', url, body);
          resolve(url);
        }
      });
    });
    req.on('error', (e) => {
      console.error('Request error for', url, e.message);
      resolve(url);
    });
    req.write(data);
    req.end();
  });
}

async function processFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  const urlRegex = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/g;
  
  const urls = content.match(urlRegex);
  if (!urls) return;

  const uniqueUrls = [...new Set(urls)].filter(u => 
    !u.includes('localhost') && 
    !u.includes('127.0.0.1') && 
    !u.includes('cryptol.ink') &&
    !u.includes('depin-hub.vercel.app') &&
    !u.includes('vercel.com') &&
    !u.includes('fonts.googleapis.com') &&
    !u.includes('logo.clearbit.com') &&
    !u.includes('cdn.tailwindcss.com') &&
    !u.includes('w3.org')
  );

  let changed = false;
  for (const url of uniqueUrls) {
    const shortUrl = await shortenUrl(url);
    if (shortUrl !== url) {
      console.log(`Replaced ${url} -> ${shortUrl}`);
      content = content.split(url).join(shortUrl);
      changed = true;
    }
    await sleep(2000); // 2 second delay between requests to be safe
  }

  if (changed) {
    fs.writeFileSync(filePath, content, 'utf8');
  }
}

async function main() {
  const dir = __dirname;
  const filesToProcess = [];
  
  function walk(currentDir) {
    const files = fs.readdirSync(currentDir);
    for (const file of files) {
      const fullPath = path.join(currentDir, file);
      if (fs.statSync(fullPath).isDirectory()) {
        if (!fullPath.includes('.git') && !fullPath.includes('node_modules') && !fullPath.includes('.vercel')) {
          walk(fullPath);
        }
      } else {
        if (fullPath.endsWith('.html') || fullPath.endsWith('.md')) {
          filesToProcess.push(fullPath);
        }
      }
    }
  }
  
  walk(dir);
  
  for (const file of filesToProcess) {
    console.log(`Processing ${file}`);
    await processFile(file);
  }
}

main().catch(console.error);
