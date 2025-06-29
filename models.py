# models.py
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, MetaData
from datetime import datetime
from database import metadata

results = Table(
    "results",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", String),  # Optional
    Column("query", String),
    Column("file_name", String),
    Column("analysis", Text),
    Column("timestamp", DateTime, default=datetime.utcnow),
)
