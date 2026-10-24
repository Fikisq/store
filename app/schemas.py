from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from typing import Annotated


class CategoryCreate(BaseModel):
    """
    Модель для создания и обновления категории.
    Используется в POST и PUT запросах.
    """
    name: Annotated[str, Field(min_length=3, max_length=50, description="Название категории (3-50 символов")]
    parent_id: Annotated[int | None, Field(description="ID родительской категории, если есть")] = None


class Category(BaseModel):
    """
    Модель для ответа с данными категории.
    Используется в GET-запросах.
    """
    id: Annotated[int, Field(description="Уникальный идентификатор категории")]
    name: Annotated[str, Field(description="Название категории")]
    parent_id: Annotated[int | None, Field(description="ID родительской категории, если есть")] = None
    is_active: Annotated[bool, Field(description="Активность категории")]

    model_config = ConfigDict(from_attributes=True)

class ProductCreate(BaseModel):
    """
     Модель для создания и обновления товара.
    Используется в POST и PUT запросах.
    """
    name: Annotated[str, Field(min_length=3, max_length=100, description="Название товара (3-100 символов)")]
    description: Annotated[str | None, Field(max_length=500, description="Описание товаров (до 500 символов")] = None
    price: Annotated[Decimal, Field(gt=0, decimal_places=2, description="Цена товара (больше 0)")]
    image_url: Annotated[str | None, Field(max_length=200, description="URL изображения товара")] = None
    stock: Annotated[int, Field(ge=0, description="Количество товаров на складе (больше 0)")]
    category_id: Annotated[int, Field(description="ID категории, к которой относится товар")]

class Product(BaseModel):
    """
    Модель для ответа с данными товара.
    Используется в GET-запросах.
    """
    id: Annotated[int, Field(description="Уникальный идентификатор товара")]
    name: Annotated[str, Field(description="Название товара")]
    description: Annotated[str | None, Field(description="Описание товара")] = None
    price: Annotated[Decimal, Field(gt=0, decimal_places=2, description="Цена товара", )]
    image_url: Annotated[str | None, Field(max_length=200, description="URL изображения товара")] = None
    stock: Annotated[int, Field(ge=0, description="Количество товаров на складе")]
    category_id: Annotated[int, Field(description="ID категории")]
    is_active: Annotated[bool, Field(description="Активность товара")]
    model_config = ConfigDict(from_attributes=True)