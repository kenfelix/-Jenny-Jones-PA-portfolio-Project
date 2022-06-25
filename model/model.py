#!/usr/bin/env python3
"""User model"""

from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Time, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    """User base Model"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    session_id = Column(String(250), nullable=True)
    login = Column(Integer, default=0)
    reset_token = Column(String(250), nullable=True)
    pa = relationship("PA", backref=backref("user", uselist=False))
    schedules = relationship('Schedule', backref='user')


class Schedule(Base):
    """Schedule base Model"""
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    start_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_date = Column(Date, nullable=False)
    end_time = Column(Time, nullable=False)
    venue = Column(String(250), nullable=True)
    reminder = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)


class PA(Base):
    """Personal assistant base Model"""
    __tablename__ = 'pa'

    id = Column(Integer, primary_key=True)
    custom_url = Column(String(50), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
