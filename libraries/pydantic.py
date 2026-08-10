class Address(BaseModel):
    city: str
    country: str
    pin_code: int

class User(BaseModel):
    user_name: int
    address: Address

from typing import Optional
from pydantic import field_validator 

class Trans(BaseModel):
    amount: float 
    note: Optional[str] = None

    @field_validator("amount")
    @ Classmethod 
    def amount_positive(cls, v):
        if v < 0:
            raise ValueError("p")
        return v 

raw_records = [
    {"user_id": 1, "email": "a@x.com"},
    {"user_id": 2, "email": "b@x.com"},
]

validated = [UserPayload(**r) for r in raw_records]
