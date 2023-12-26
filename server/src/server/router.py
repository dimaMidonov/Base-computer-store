from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *

routers = (
    RouterManager(
        database_model=database_models.User,
        pydantic_model=pydantic_models.User
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Address,
        pydantic_model=pydantic_models.Address
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Product,
        pydantic_model=pydantic_models.Product
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Category,
        pydantic_model=pydantic_models.Category
    ).fastapi_router,

    RouterManager(
        database_model=database_models.ProductCategory,
        pydantic_model=pydantic_models.ProductCategory
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Order,
        pydantic_model=pydantic_models.Order
    ).fastapi_router,

    RouterManager(
        database_model=database_models.OrderItem,
        pydantic_model=pydantic_models.OrderItem
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Review,
        pydantic_model=pydantic_models.Review
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Wishlist,
        pydantic_model=pydantic_models.Wishlist
    ).fastapi_router,
)
