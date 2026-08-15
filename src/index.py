def get_odd_numbers(numbers: list[int]) -> list[int]:
    odds = []
    for number in numbers:
        if number % 2 != 0:
            odds.append(number)
    return odds

def count_char_frequency(text: str) -> dict[str, int]:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sum_key_values(dict_list: list[dict], target_key: str) -> int:
    total = 0
    for item in dict_list:
        if target_key in item:
            total += item[target_key]
    return total

def remove_duplicates(items: list[str]) -> list[str]:
    cleaned = []
    for item in items:
        if item not in cleaned:
            cleaned.append(item)
    return cleaned

def reverse_words(sentence: str) -> str:
    words = sentence.split()
    return " ".join(reversed(words))



-- 1. Customers with orders over $100
SELECT customer_id, total_amount
FROM orders
WHERE total_amount > 100;

-- 2. Order count per customer, most to fewest
SELECT customer_id, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;

-- 3. Average order value per region (region lives in customers table — needs a join)
SELECT c.region, AVG(o.total_amount) AS avg_order_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region;

-- 4. Orders placed in the last 30 days
SELECT *
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days';

-- 5. Customers who have never placed an order
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;



import pandas as pd

# 1. Filter rows where amount > 50
filtered_df = df[df['amount'] > 50]

# 2. Average price per category
avg_price_by_category = df.groupby('category')['price'].mean()

# 3. Add a total column (quantity * price)
df['total'] = df['quantity'] * df['price']

# 4. Drop rows where email is null
cleaned_df = df.dropna(subset=['email'])

# 5. Sort by date descending
sorted_df = df.sort_values('date', ascending=False)



import requests

# 1. Basic GET with error handling
response = requests.get("https://api.example.com/v1/users", timeout=10)
response.raise_for_status()
data = response.json()

# 2. GET with query parameters
response = requests.get(
    "https://api.example.com/v1/orders",
    params={"status": "completed", "limit": 50},
    timeout=10
)
response.raise_for_status()
orders = response.json()

# 3. POST with a JSON body and auth header
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.post(
    "https://api.example.com/v1/records",
    json={"name": "test", "value": 42},
    headers=headers,
    timeout=10
)
response.raise_for_status()

# 4. Paginated fetch
def fetch_all_pages(base_url: str) -> list[dict]:
    results, page = [], 1
    while True:
        resp = requests.get(base_url, params={"page": page}, timeout=10)
        resp.raise_for_status()
        batch = resp.json().get("results", [])
        if not batch:
            break
        results.extend(batch)
        page += 1
    return results

# 5. Handling a failed request gracefully
try:
    response = requests.get("https://api.example.com/v1/status", timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    data = None



from pydantic import BaseModel, Field, field_validator
from typing import Optional

# 1. Basic model with a required field constraint
class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float
    in_stock: bool = True


# 2. Nested model
class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    user_id: int
    address: Address


# 3. Optional field + default value
class Transaction(BaseModel):
    amount: float
    note: Optional[str] = None


# 4. Custom field validation
class Order(BaseModel):
    quantity: int

    @field_validator("quantity")
    @classmethod
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("quantity must be positive")
        return v


# 5. Validating a list of raw dicts into models
raw_records = [
    {"name": "widget", "price": 9.99},
    {"name": "gadget", "price": 19.99},
]
validated_products = [Product(**r) for r in raw_records]
