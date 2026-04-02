import json
import time
from playwright.sync_api import sync_playwright

COOKIE_FILE = "depin-hub/scripts/twitter_cookies.json"
SEARCH_URL = "https://x.com/search?q=%28%22giveaway%22%20OR%20%22win%20a%22%29%20%28%22DePIN%22%20OR%20%22BitAxe%22%20OR%20%22ASIC%22%20OR%20%22NerdMiner%22%20OR%20%22Scrypt%22%20OR%20%22SHA256%22%20OR%20%22LuckyMiner%22%20OR%20%22mining%22%20OR%20%22hardware%22%20OR%20%22node%22%20OR%20%22SOL%22%29%20-mint%20-pfp%20min_faves%3A10%20within_time%3A48h&src=typed_query&f=top"

def run():
    with open(COOKIE_FILE, "r") as f:
        cookies = json.load(f)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.add_cookies(cookies)
        page = context.new_page()
        page.goto(SEARCH_URL, wait_until="networkidle")
        time.sleep(8)
        tweets = page.query_selector_all('article[data-testid="tweet"]')
        print(f"Found {len(tweets)} tweets")
        for tweet in tweets[:5]:
            text_el = tweet.query_selector('div[data-testid="tweetText"]')
            print("---")
            if text_el:
                print(text_el.inner_text().replace("\n", " ")[:150])
        browser.close()

run()
