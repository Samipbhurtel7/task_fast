from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from application.schema import Article as ArticleSchema
from application.database import SessionLocal
from application.util import add_article as save
from application.util import get_articles as get_all
from application.util import get_article as get_by_id
from application.util import delete_article
from application.util import update_article

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/article")
def add_article(article: ArticleSchema, db: Session = Depends(get_db)):
    save(article, db)

@router.get("/articles")
def get_all_article(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/article/{id}")
def get_article_by_id(id: str, db: Session = Depends(get_db)):
    return get_by_id(id, db)


@router.delete("/article/{id}")
def remove_article_by_id(id: str, db: Session = Depends(get_db)):
    return delete_article(id, db)

@router.put("/article/{id}")
def update_article_by_id(article: ArticleSchema, id: str, db: Session = Depends(get_db)):
    return update_article(id, article, db)
