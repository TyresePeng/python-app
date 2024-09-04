from sqlalchemy import (
    create_engine,
    BigInteger,
    Column,
    Integer,
    DateTime,
    String,
)
import datetime
from sqlalchemy.orm import declarative_base

# 创建对象的基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'test_user'

    id = Column(Integer, primary_key=True, comment="主建")
    name = Column(String(255), nullable=True,comment="姓名")
    age = Column(Integer, nullable=True,comment="年龄")
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now,comment="创建时间")
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now, index=True,comment="修改时间")
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age}, create_time={self.create_time}, update_time={self.update_time})>"


