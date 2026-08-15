import requests

response = requests.get("https://api.example.com/v1/users", timeout=10)
response.raise_for_status()
data = response.json() 

response = requests.get(
    "https://api.example.com/v1/users",
    perams={"status": "completed", "limit": 50},
    timeout=10
)
response.raise_for_status()
orders = response.json()

headers = {"Authorization": f"Bearer {api_token}"}
response = requests.post(
    "https://api.example.com/v1/users",
    json={
        "name": "test",
        "value": 42
    },
    headers=headers,
    timeout=10
)
response.raise_for_status()

def fetch_all_pages(base_url: str) -> list[dict]:
    results, page = [], 1 
    while True:
        resp = requests.get(base_url, perams={"page": page}, timeout=10)
        resp.raise_for_status()
        batch = resp.json().get("results", [])
        if not batch:
            break
        results.extend(batch)
        page += 1 
    return results

try: 
    response = requests.get("https://api.example.com/v1/status", timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    data = None
