import requests
import os
import time
from datetime import datetime, timedelta, timezone
import json

# --- Configuration ---
TELEGRAM_USER_ID = "5269660297"
TAVILY_API_KEY = "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" 
MARKET_API_URL = "https://gamma-api.polymarket.com/markets" 
PUBLIC_MARKET_URL = "https://clob.polymarket.com/markets" 
MAX_POLL_INTERVAL_SECONDS = 1800  # 30 minutes
MAX_BET_USD = 50.0
MIN_BET_USD = 20.0
TIME_TO_SETTLE_THRESHOLD_SECONDS = 24 * 3600 # < 24 hours

# --- Core Functions ---

def get_market_data():
    """
    Mocks market data fetch, dynamically setting settlement time to ensure alerts are generated,
    using structure inferred from the live site snapshot.
    """
    
    # Set settlement time to be ~10 hours in the future
    now_utc = datetime.now(timezone.utc)
    close_settlement = now_utc + timedelta(hours=10, minutes=30)
    
    return [
        {
            "id": "live_mock_1",
            "question": "Will the US strike 3 countries in February 2026?", # From snapshot, showing 100% Yes
            "end_date_iso": close_settlement.isoformat(), # Should trigger
            "tokens": [
                {"outcome": "Yes", "price": 0.98}, # High price, sentiment is mixed -> Should trigger Overprice alert
                {"outcome": "No", "price": 0.02}
            ]
        },
        {
            "id": "live_mock_2",
            "question": "Will the price of Crude Oil (CL) hit $100 by end of March?", # From snapshot, showing 22% Yes
            "end_date_iso": close_settlement.isoformat(), # Should trigger
            "tokens": [
                {"outcome": "Yes", "price": 0.10}, # Low price, sentiment is bullish -> Should trigger Underprice alert
                {"outcome": "No", "price": 0.90}
            ]
        }
    ]

def fetch_sentiment_via_web_search(query: str) -> dict:
    """Returns hardcoded mock sentiment based on market question."""
    if "ETH" in query or "Crude Oil" in query:
        # Mocking a bullish sentiment for the oil market (underpriced)
        return {"sentiment": "bullish", "keywords": ["strong_demand", "positive_news"]}
    elif "Iran" in query:
        # Mocking a mixed/bearish sentiment for the Iran market (overpriced)
        return {"sentiment": "mixed", "keywords": ["sell pressure", "negative_news"]}
    return {"sentiment": "neutral", "keywords": []}

def calculate_arbitrage_ev(market, sentiment_data):
    """Calculates potential EV based on price vs external sentiment."""
    
    yes_token = next((t for t in market.get('tokens', []) if t.get('outcome') == 'Yes'), None)
    no_token = next((t for t in market.get('tokens', []) if t.get('outcome') == 'No'), None)
    
    if not yes_token or not no_token:
        return None

    p_yes = yes_token.get('price', 0.5)
    
    alert = None
    
    if p_yes > 0.75 and sentiment_data['sentiment'] in ["mixed", "bearish"]:
        potential_bet_size = MAX_BET_USD
        alert = f"**HIGH ALERT (Potential Overprice/Lagging News)**\nMarket: {market.get('question', market.get('title', 'Unknown Market'))}\nPrice(Yes): {p_yes:.2f} (Implied {p_yes*100:.0f}%)\nSentiment: {sentiment_data['sentiment']} ({', '.join(sentiment_data['keywords'][:2])})\nPotential Action: Short 'Yes' / Bet ${potential_bet_size} on 'No'."
        
    elif p_yes < 0.25 and sentiment_data['sentiment'] in ["bullish"]:
        potential_bet_size = MAX_BET_USD
        alert = f"**HIGH ALERT (Potential Underprice/Lagging News)**\nMarket: {market.get('question', market.get('title', 'Unknown Market'))}\nPrice(Yes): {p_yes:.2f} (Implied {p_yes*100:.0f}%)\nSentiment: {sentiment_data['sentiment']} ({', '.join(sentiment_data['keywords'][:2])})\nPotential Action: Long 'Yes' / Bet ${potential_bet_size} on 'Yes'."

    return alert

def send_alert_to_telegram(alert_text, market_question):
    """Sends a message using the print output capture method."""
    print(f"TELEGRAM_ALERT_START|ID:{TELEGRAM_USER_ID}|MESSAGE_TYPE:ArbHunter")
    print(alert_text)
    print("TELEGRAM_ALERT_END")


def main_loop():
    print(f"PolyArb Hunter starting. Checking markets...")
    
    markets = get_market_data()
    
    quick_markets = []
    
    # 1. Filter by Settlement Time (< 24h)
    now_utc = datetime.now(timezone.utc)
    for market in markets:
        try:
            end_date_str = market.get('end_date_iso', '') 
            
            if not end_date_str:
                continue 

            end_date_str = end_date_str.replace('Z', '+00:00')
            settle_time = datetime.fromisoformat(end_date_str)
            
            time_left = (settle_time - now_utc).total_seconds()
            
            if 0 < time_left < TIME_TO_SETTLE_THRESHOLD_SECONDS:
                market['time_left_seconds'] = time_left
                quick_markets.append(market)
            else:
                pass
                
        except ValueError as e:
            print(f"Warning: Could not parse date for market {market.get('id', 'unknown')}: {e}")
            continue

    if not quick_markets:
        print("No quick-settle markets (<24h) found.")
        return

    print(f"Found {len(quick_markets)} markets settling in <24 hours.")
    
    alerts = []
    
    # 2. Analyze quick markets (Sentiment & EV Calculation)
    for market in quick_markets:
        question = market.get('question', market.get('title', 'No Question Provided'))
        
        sentiment = fetch_sentiment_via_web_search(question)
        alert_text = calculate_arbitrage_ev(market, sentiment)
        
        if alert_text:
            formatted_alert = (
                f"**TIME LEFT: {market['time_left_seconds'] / 3600:.1f}h**\n"
                f"Q: {question}\n"
                f"{alert_text}"
            )
            alerts.append(formatted_alert)

    # 3. Output Top 3 Alerts
    if alerts:
        print(f"--- Potential Arbitrage/Inefficiency Alerts ({len(alerts)} found) ---")
        
        top_alerts = alerts[:3]
        
        for i, alert in enumerate(top_alerts):
            print(f"\n--- ALERT {i+1} ---")
            print(alert)
            send_alert_to_telegram(alert, question)
    else:
        print("No significant arbitrage opportunities flagged based on current heuristics.")

if __name__ == "__main__":
    main_loop()