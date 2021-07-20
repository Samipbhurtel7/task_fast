from typing import Optional, Dict, List
from datetime import datetime
from pydantic import BaseModel

class Author(BaseModel):
    id: str
    username: str

class Content(BaseModel):
    season: List[Dict]
    description: str

class Article(BaseModel):
    id: str
    address: str
    content: Optional[Content]
    author: Author
    created: datetime
    updated: Optional[datetime]
    counters: Dict[str, int]
    