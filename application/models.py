from sqlalchemy import Column, String, JSON, Integer
from application.database import Base


class Article(Base):
    __tablename__ = "article_table"
    id = Column(String, primary_key=True, index=True)
    path = Column(String, nullable=False)
    seasons = Column(JSON)
    body = Column(String)
    author_name = Column(String, nullable=False)
    author_id = Column(String, nullable=False)
    created_date = Column(String, nullable=False)
    created_time = Column(String, nullable=False)
    updated_date = Column(String)
    updated_time = Column(String)
    counters_total = Column(Integer, nullable=False)
