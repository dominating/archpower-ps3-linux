import re
with open("depin-hub/scripts/update_x_giveaways.py", "r") as f:
    code = f.read()
code = re.sub(r'SEARCH_URL = ".*?"', 'SEARCH_URL = "https://x.com/search?q=%28%22giveaway%22%20OR%20%22win%22%20OR%20%22airdrop%22%29%20%28%22DePIN%22%20OR%20%22BitAxe%22%20OR%20%22ASIC%22%20OR%20%22NerdMiner%22%20OR%20%22Scrypt%22%20OR%20%22SHA256%22%20OR%20%22LuckyMiner%22%20OR%20%22Lucky%20Miner%22%20OR%20%22mining%20hardware%22%20OR%20%22validator%20node%22%20OR%20%22node%20license%22%29%20-mint%20-pfp%20-NFT%20-NFTs%20min_faves%3A10%20within_time%3A48h&src=typed_query&f=top"', code, count=1)
with open("depin-hub/scripts/update_x_giveaways.py", "w") as f:
    f.write(code)
