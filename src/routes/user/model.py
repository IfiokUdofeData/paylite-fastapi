from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, DateTime, Text, Index
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    language_preference = Column(String(50), ForeignKey('languages.language_id'), nullable=True)
    dialect_preference = Column(Integer, ForeignKey('dialects.dialect_id'), nullable=True)
    
    dialects = relationship("Dialect", secondary='user_dialects')

class Dialect(Base):
    __tablename__ = 'dialects'
    dialect_id = Column(Integer, primary_key=True, autoincrement=True)
    dialect_name = Column(String(100), nullable=False)
    dialect_description = Column(Text, nullable=True)

class UserDialect(Base):
    __tablename__ = 'user_dialects'
    user_dialect_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    dialect_id = Column(Integer, ForeignKey('dialects.dialect_id', ondelete='CASCADE'), nullable=False)

class Account(Base):
    __tablename__ = 'accounts'
    account_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True)
    account_type = Column(Enum('savings', 'current'), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    account_balance = Column(DECIMAL(18, 2), nullable=False)

    __table_args__ = (
        Index('ix_user_id_account_type', 'user_id', 'account_type'),
    )