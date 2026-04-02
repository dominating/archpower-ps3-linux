import urllib.parse
query = '(DePIN OR ASIC OR GPU OR "Lucky Miner" OR "mining hardware" OR "AI node" OR "NerdMiner" OR crypto) (giveaway OR airdrop) -NFT -NFTs -mint min_faves:20 within_time:48h'
print(f"https://x.com/search?q={urllib.parse.quote(query)}&src=typed_query&f=top")
