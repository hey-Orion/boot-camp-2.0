ok here are the codes i have writen these by looking right now
and here are my questions on these codes answer the questions then
ill try to write the codes by myself


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



select customer_id, total_amount
from orders 
where total_amount >= 100;

select customer_id, count(*) as total_orders
from orders
group by customer_id
order by total_orders desc;

select c.region, avg(o.total_amount) as avg_order_amount
from orders o 
join customers c on o.customer_id = c.customer_id
group by c.region;

select * 
from orders
where order_date >= current_date - interval '30 days';

select c.customer_id, c.name
from customers c 
left join orders o on c.customer_id = o.customer_id
where o.customer_id is NULL;



import pandas as pd 

filtered_df = df[df['amount'] > 50]

avg_price_by_category = df.groupby('category')['price'].mean()

df['total'] = df['quantity'] * df['price']

cleaned_df = df.dropna(subset=['email'])

sorted_df = df.sort_values('date', ascending=False)



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



from pydantic import BaseModel, Field, field_validator
from typing import Optional

class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float
    in_stock: bool = True

class Address(BaseModel):
    city: str 
    country: str 

class User(BaseModel):
    user_id: int 
    address: Address

class Transaction(BaseModel):
    amount: float
    note: Optional[str] = None

class Order(BaseModel):
    quantity: int 

    @field_validator("quantity")
    @classmethod
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("quantity must be positive")
        return v 

raw_records = [
    {"name": "widget", "price": 9.99},
    {"name": "gadget", "price": 19.99},
]
validated_products = [Product(**r) for r in raw_records]
























