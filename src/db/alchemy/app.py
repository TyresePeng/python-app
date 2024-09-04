from src.db.alchemy.connecte.connected import Session,engine
from src.db.alchemy.entity.User import User

Base = User.__base__
Base.metadata.create_all(engine)

for i in range(5):
    with Session() as session:
        new_user = User(name="张三", age=22)
    session.add(new_user)
    session.commit()
    print(f"User 张三 created.")

with Session() as session:
    # 查询所有用户
    result = session.query(User).all()
    for user in result:
        print(user)
