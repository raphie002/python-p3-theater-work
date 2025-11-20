# lib/database.py
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

# 🚀 Connect to a SQLite database file named 'auditions.db'
# The 'check_same_thread=False' is needed for SQLite multi-threading access
# The engine translates Python into SQL
engine = create_engine('sqlite:///auditions.db', echo=True, connect_args={"check_same_thread": False})

# 🤝 Create a configured 'Session' class
Session = sessionmaker(bind=engine)

# ➡️ Create a Session
session = Session()