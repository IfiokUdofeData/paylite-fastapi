from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, DateTime, Text, Index
from sqlalchemy.orm import relationship
from database import Base

class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)
    role_description = Column(Text, nullable=True)

class UserRole(Base):
    __tablename__ = 'users_roles'
    user_role_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.role_id', ondelete='CASCADE'), nullable=False)

    user = relationship("User")
    role = relationship("Role")

class AccessToken(Base):
    __tablename__ = 'access_tokens'
    access_token_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True)
    access_token = Column(String(255), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)

    user = relationship("User")

    __table_args__ = (
        Index('ix_user_id_access_token', 'user_id', 'access_token'),
    )