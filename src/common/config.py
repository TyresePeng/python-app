def get_message():
    return "Hello from config.py file!"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.1:3306/test_db?charset=utf8"  # SQLAlchemy 数据库连接串，格式见下面
SQLALCHEMY_ECHO = "True"  # 是不是要把所执行的SQL打印出来，一般用于调试
SQLALCHEMY_POOL_SIZE = "5"  # 连接池大小
SQLALCHEMY_POOL_MAX_SIZE = "20"  # 连接池最大的大小
SQLALCHEMY_POOL_RECYCLE = "3600"  # 多久时间主动回收连接，见下注释

