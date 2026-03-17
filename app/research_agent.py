import requests
from config.config import SERPER_API_KEY

def search_topic(topic):
    
    url = "https://google.serper.dev/search"
    payload = {
        "q": topic
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    snippets = []

    if "organic" in data:
        for result in data["organic"]:
            snippets.append(result.get("snippet", ""))

    return "\n".join(snippets)