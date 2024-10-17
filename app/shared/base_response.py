from typing import Any
from pydantic import BaseModel

class BaseResponse(BaseModel):
    message: str
    success: bool = True
    data: Any = None
    error: Any = None