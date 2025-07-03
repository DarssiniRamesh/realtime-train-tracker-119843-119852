"""
SQLAlchemy ORM model for the User.

Includes fields for username/email, password hash, registration time, and optional user profile data.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

from ..api.main import Base

# PUBLIC_INTERFACE
class User(Base):
    """Database model for users with secure password storage."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
