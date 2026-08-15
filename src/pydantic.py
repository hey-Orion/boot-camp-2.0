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