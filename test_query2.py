import urllib.parse
query = '("giveaway" OR "win a") ("DePIN" OR "BitAxe" OR "ASIC" OR "NerdMiner" OR "Scrypt" OR "SHA256" OR "LuckyMiner" OR "mining" OR "hardware" OR "node" OR "SOL") -mint -pfp min_faves:20 within_time:24h'
print(f"https://x.com/search?q={urllib.parse.quote(query)}&src=typed_query&f=top")
