from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, DateTime, Text, Index
from sqlalchemy.orm import relationship
from database import Base

class MLModel(Base):
    __tablename__ = 'ml_models'
    model_id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(255), nullable=False)
    model_type = Column(Enum('classification', 'regression'), nullable=False)
    model_description = Column(Text, nullable=True)

class MLModelVersion(Base):
    __tablename__ = 'ml_model_versions'
    model_version_id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('ml_models.model_id', ondelete='CASCADE'), nullable=False)
    version_number = Column(String(50), nullable=False)
    model_parameters = Column(JSON, nullable=False)
    model_weights = Column(Text, nullable=False)

    model = relationship("MLModel")
