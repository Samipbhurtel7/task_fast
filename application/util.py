import logging
from sqlalchemy.orm import Session
from application.schema import Article as ArticleSchema
from application.models import Article as ArticleModel

def add_article(article: ArticleSchema, db: Session):
    model = ArticleModel(
        id = article.id,
        path = article.address,
        seasons = article.content.season if article.content and article.content.season else None,
        body = article.content.description if article.content and article.content.description else None,
        author_name = article.author.username,
        author_id = article.author.id,
        created_date = str(article.created.date()),
        created_time = str(article.created.time()),
        counters_total = sum(article.counters.values())
    )
    if article.updated:
        model.updated_date = str(article.updated.date()),
        model.updated_time = str(article.updated.time()),
    try:
        db.add(model)
        db.commit()
    except Exception as err:
        logging.error(err)

def delete_article(id: str, db: Session):
    try:
        row = get_article(id, db)
        if row:
            db.delete(row)
            db.commit()
    except Exception as err:
        logging.error(err)

def update_article(id: str, article: ArticleSchema, db: Session):
    try:
        row = get_article(id, db)
        if row:
            row.path = article.address,
            row.seasons = article.content.season if article.content and article.content.season else None,
            row.body = article.content.description if article.content and article.content.description else None,
            row.author_name = article.author.username,
            row.author_id = article.author.id,
            row.created_date = article.created.date(),
            row.created_time = article.created.time(),
            if article.updated:
                row.updated_date = article.updated.date(),
                row.updated_time = article.updated.time(),
            row.counters_total = sum(article.counters.values())
            db.commit()
    except Exception as err:
        logging.error(err)

def get_articles(db: Session):
    return db.query(ArticleModel).all()

def get_article(id: str, db: Session):
    return db.query(ArticleModel).filter(ArticleModel.id == id).first()
