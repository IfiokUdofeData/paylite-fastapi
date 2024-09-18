from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, DateTime, Text, Index
from sqlalchemy.orm import relationship
from database import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id', ondelete='CASCADE'), nullable=False, index=True)
    transaction_type = Column(Enum('deposit', 'withdrawal', 'transfer'), nullable=False)
    transaction_amount = Column(DECIMAL(18, 2), nullable=False)
    transaction_date = Column(DateTime, index=True, nullable=False)
    transaction_status = Column(Enum('pending', 'completed', 'failed'), nullable=False)

    account = relationship("Account")

class Payment(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey('transactions.transaction_id', ondelete='CASCADE'), nullable=False, index=True)
    payment_method = Column(Enum('SMS', 'USSD', 'card', 'online'), nullable=False)
    payment_status = Column(Enum('pending', 'completed', 'failed'), nullable=False)

    transaction = relationship("Transaction")