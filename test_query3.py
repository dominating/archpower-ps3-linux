import urllib.parse
query = '("giveaway" OR "win" OR "airdrop") ("DePIN" OR "BitAxe" OR "ASIC" OR "NerdMiner" OR "Scrypt" OR "SHA256" OR "LuckyMiner" OR "Lucky Miner" OR "mining hardware" OR "validator node" OR "node license") -mint -pfp -NFT -NFTs min_faves:10 within_time:72h'
print(f"https://x.com/search?q={urllib.parse.quote(query)}&src=typed_query&f=top")
