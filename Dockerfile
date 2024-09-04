# 使用官方的Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有内容到工作目录
COPY . /app

# 安装所需的Python包
RUN pip install flask redis

# 暴露应用运行的端口
EXPOSE 5000

# 设置容器启动时运行的命令
CMD ["python", "src/app.py"]

