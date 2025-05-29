from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Resp(BaseModel):
    body: str
    name: str
    letter_id: Optional[str]
    created_at: datetime
