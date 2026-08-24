from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Optional

class All_BS(BaseModel):
    city: str 
    country: str 
    pin_code: int 
    user_id: int 
    name: str 
    id: int 
    price: float 
    description: Optional[str] = None
    is_available: Optional[bool] = None
    age: int = Field(gt=19) what dose gt stand for 
    salary: float = Field(gt=0)

class Registration(BaseModel):
    username: str
    email: str 

    @field_validator("username") just tell me whatt is this block doing nothing else 
    @classmethod
    def validate_username(cls, v) -> str:
        if len(v) < 3:
            raise ValueError("..............")
        return v.lower()

class Order(BaseModel):
    item_price: float
    quantity: int 

    @computed_field what is self what dose it stands for 
    @property
    def total_price(self) -> float:
        return self.item_price * self.quantity