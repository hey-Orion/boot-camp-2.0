def summarize_by_user(transactions: list[dict]) -> dict:
    summary = {}
    for t in transactions:
        user = t["user_id"]
        amount = t.get("amount", 0)
        if user not in summary:
            summary[user] = {"total": 0, "count": 0}
        summary[user]["total"] += amount
        summary[user]["count"] += 1

    return {
        user: {
            "total": data["total"],
            "average": round(data["total"] / data["count"], 2)
        }
        for user, data in summary.items()
    }

def clean_records(records: list[dict]) -> tuple[list[dict], list[str]]:
    """Return (valid_records, error_messages) instead of raising on first bad record."""
    valid = []
    errors = []
    for i, r in enumerate(records):
        try:
            if "amount" not in r or r["amount"] is None:
                raise ValueError("missing amount")
            amount = float(r["amount"])
            if amount < 0:
                raise ValueError("negative amount")
            valid.append({**r, "amount": amount})
        except (ValueError, TypeError) as e:
            errors.append(f"record {i}: {e}")
    return valid, errors


mean = df["amount"].mean()
std = df["amount"].std()
df["is_outlier"] = (df["amount"] - mean).abs() > 3 * std
outliers = df[df["is_outlier"]]

df["amount"] = df.groupby("user_id")["amount"].transform(
    lambda x: x.fillna(x.mean())
)


import requests
from time import sleep 

def fetch_with_retry(url: str, retries: int = 3) -> dict:
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestsException:
            if attempt == retries - 1:
                raise 
            sleep(1)

payload = {"user_id": 1, "event": "purchase"}
response = requests.post("url", json=payload, timeout=5)

if response.status_code == 201:
    print("created:", response.json)
else:
    print("failed:", response.status_code, response.text)


from pydantic import BaseModel, Field 
from datetime import datetime

class Event(BaseModel):
    event_id: int 
    event_type: str 
    created_at: datetime = Field(default_factory=datetime.utcnow)


from pydantic import ValidationError

def validate_batch(raw_records: list[dict]) -> list[Event]:
    valid = []

    for r in raw_records:
        try:
            valid.append(Event(**r))
        except ValidationError:
            continue
    return valid


from sqlalchemy.orm import Session

rew_pipeline = Pipeline(name="daily_ingest", active=True)

with Session(engine) as session: 
    session.add(new_pipeline)
    session.commit()

with Session(engine) as session:
    recent_active = (
        session.query(Pipeline)
        .filter(Pipeline.active == True)
        .order_by(Pipeline.id.desc())
        .limit(10)
        .all()
    )


def test_clean_records_flags_negative_amount():
    records = [{"amount": -5}]
    valid, error = clean_records(records) 
    assert valid == []
    assert "negative amount" om errors[0]

import pytest

@pytest.fixture
def sample_transactions():
    return [
        {"user_id": 1, "amount": 50},
        {"user_id": 1, "amount": 30},
        {"user_id": 2, "amount": 20},
    ]

def test_summarize_by_user_totals(sample_transactions):
    result = summarize_by_user(sample_transactions)
    assert result[1]["total"] == 80
    assert result[2]["total"] == 20
    


