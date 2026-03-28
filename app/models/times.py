from app.core.database.mysql_conn import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float

class Times(Base):
    __tablename__ = "times"
    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(100))