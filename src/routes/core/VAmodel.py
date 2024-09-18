from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, DateTime, Text, Index
from sqlalchemy.orm import relationship
from database import Base

class VirtualAssistant(Base):
    __tablename__ = 'virtual_assistants'
    virtual_assistant_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

class Intent(Base):
    __tablename__ = 'intents'
    intent_id = Column(Integer, primary_key=True, autoincrement=True)
    virtual_assistant_id = Column(Integer, ForeignKey('virtual_assistants.virtual_assistant_id', ondelete='CASCADE'), nullable=False)
    intent_name = Column(String(255), nullable=False)
    intent_description = Column(Text, nullable=True)

    virtual_assistant = relationship("VirtualAssistant")

class Entity(Base):
    __tablename__ = 'entities'
    entity_id = Column(Integer, primary_key=True, autoincrement=True)
    intent_id = Column(Integer, ForeignKey('intents.intent_id', ondelete='CASCADE'), nullable=False)
    entity_name = Column(String(255), nullable=False)
    entity_type = Column(String(255), nullable=False)

    intent = relationship("Intent")