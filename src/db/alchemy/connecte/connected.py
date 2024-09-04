from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import src.common.config as config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,  # SQLAlchemy 数据库连接串，格式见下面
    echo=bool(config.SQLALCHEMY_ECHO),  # 是不是要把所执行的SQL打印出来，一般用于调试
    pool_size=int(config.SQLALCHEMY_POOL_SIZE),  # 连接池大小
    max_overflow=int(config.SQLALCHEMY_POOL_MAX_SIZE),  # 连接池最大的大小
    pool_recycle=int(config.SQLALCHEMY_POOL_RECYCLE),  # 多久时间主动回收连接，见下注释
)
Session = sessionmaker(bind=engine)

