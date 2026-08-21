from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Optional

class Address(BaseModel):
    city: str 
    country: str 
    pin_code: Optional[str] = None 

class User(BaseModel):
    user_id: int 
    name: str
    address: Address

class Product(BaseModel):
    id: int 
    name: str 
    price: float
    description: Optional[str] = None
    is_available: bool = True

class Employee(BaseModel):
    email: str 
    age: int Field(gt=18)
    salary: float Field(gt=0)

class Registration(BaseModel):
    username: str 
    email: str 

    @field_validator('username')
    @classmethod
    def validate_username(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters")
        return v.lower()

class Order(BaseModel):
    item_price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.item_price * self.quantity

