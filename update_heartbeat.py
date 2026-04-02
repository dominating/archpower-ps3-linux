import json

with open('memory/heartbeat-state.json', 'r') as f:
    data = json.load(f)

# Update scout to the current timestamp (approx 2026-03-30 09:28 UTC -> ~1774862880)
# Actually, I'll just use a python script to get current timestamp
import time
data['lastChecks']['scout'] = int(time.time())

with open('memory/heartbeat-state.json', 'w') as f:
    json.dump(data, f, indent=2)
