"""
CRUD functions for user management: registration, login, and fetching users.
"""

from sqlalchemy.orm import Session
from ..models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# PUBLIC_INTERFACE
def get_user_by_username(db: Session, username: str):
    """Fetch a user from the DB by username."""
    return db.query(User).filter(User.username == username).first()

# PUBLIC_INTERFACE
def get_user_by_email(db: Session, email: str):
    """Fetch a user from the DB by email."""
    return db.query(User).filter(User.email == email).first()

# PUBLIC_INTERFACE
def create_user(db: Session, username: str, email: str, password: str):
    """Register a new user and hash the password before storing."""
    hashed_pw = pwd_context.hash(password)
    db_user = User(username=username, email=email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# PUBLIC_INTERFACE
def verify_password(plain_password, hashed_password):
    """Verify if a plain password matches the hash."""
    return pwd_context.verify(plain_password, hashed_password)

# PUBLIC_INTERFACE
def authenticate_user(db: Session, username: str, password: str):
    """Check user credentials and return user if valid, else None."""
    user = get_user_by_username(db, username)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
