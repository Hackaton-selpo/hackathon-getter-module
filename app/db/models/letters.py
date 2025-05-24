from sqlalchemy import Column, DateTime, String

from app.db.database import Base

class Letters(Base):
    __tablename__ = "letters"

    id = Column(String, primary_key=True)
    date = Column(DateTime)
    author = Column(String)
    text = Column(String)
    url = Column(String)
    sender = Column(String)
    recipient = Column(String)
    destination = Column(String)
