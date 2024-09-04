from flask import Flask
import common.config as config
import src.db.alchemy.db as db
from common.response import Response
app = Flask(__name__)
app.json.ensure_ascii = False # 解决中文乱码问题

@app.get('/')
def hello_from_config():
    # 从 config.py 获取消息
    # 返回来自 config.py 和 Redis 的信息
    return Response.error(config.get_message())

@app.get('/health/check')
def health_check():
    # 从 config.py 获取消息
    return Response.success("成功")

@app.get('/user/list')
def user_list():
    return Response.success(db.user_list())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
