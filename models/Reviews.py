from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from database import metadata

reviews = Table(
    "reviews",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("book_id", Integer, ForeignKey('books.id')),
    Column("rating", Integer),
    Column("review_text", String),
    Column("created_at", DateTime, default=datetime.utcnow)
)