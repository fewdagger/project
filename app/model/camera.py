from typing import Optional, List
from pydantic import BaseModel, Field


class createCameraModel(BaseModel):
    id: str = Field(min_length=8, max_length=8)
    brand: str
    name: str
    price: float
    color: str


class updateCameraModel(BaseModel):
    brand: Optional[str]
    name: Optional[str]
    price: Optional[float]
    color: Optional[str]