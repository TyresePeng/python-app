from flask import jsonify
import time


class Response:
    """统一返回结果类"""
    SUCCESS = 200
    ERROR = 500

    def __init__(self, status: int, message: str, data: any = None):
        """
        初始化返回结果类的属性
        :param status: 状态码，通常用来表示结果是否成功
        :param message: 返回的信息，给用户的提示
        :param data: 返回的数据,默认为None
        """
        self.status = status
        self.message = message
        self.data = data
        self.timestamp = int(time.time() * 1000)

    def to_dict(self):
        """将返回结果类的实例转化为字典格式"""
        return {
            'status': self.status,
            'message': self.message,
            'data': self.data,
            'timestamp': self.timestamp,
        }

    @staticmethod
    def success(data=None, message="success"):
        """构造一个成功的响应"""
        response = jsonify(Response(Response.SUCCESS, message, data).to_dict())
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    @staticmethod
    def error(message="error", data=None):
        """构造一个失败的响应"""
        response = jsonify(Response(Response.ERROR, message, data).to_dict())
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
