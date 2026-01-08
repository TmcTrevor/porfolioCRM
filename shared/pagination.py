from typing import Generic, TypeVar, List
from pydantic import BaseModel

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response model."""
    items: List[T]
    page: int
    limit: int
    total: int
