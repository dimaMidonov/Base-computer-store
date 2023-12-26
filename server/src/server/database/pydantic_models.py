from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: int = 1


class User(BaseModelModify):
    username: str
    email: str
    password: str
    role: str
    created_at: str


class Address(BaseModelModify):
    user_id: int
    street: str
    city: str
    state: str
    zip_code: str
    created_at: str


class Product(BaseModelModify):
    name: str
    description: str
    price: float
    stock_quantity: int
    created_at: str


class Category(BaseModelModify):
    name: str
    description: str
    created_at: str


class ProductCategory(BaseModelModify):
    product_id: int
    category_id: int
    created_at: str


class Order(BaseModelModify):
    user_id: int
    address_id: int
    order_date: str
    total_amount: float
    status: str
    created_at: str


class OrderItem(BaseModelModify):
    order_id: int
    product_id: int
    quantity: int
    subtotal: float
    created_at: str


class Review(BaseModelModify):
    product_id: int
    user_id: int
    rating: int
    comment: str
    created_at: str


class Wishlist(BaseModelModify):
    user_id: int
    product_id: int
    created_at: str

