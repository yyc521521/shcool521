import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    JSON_AS_ASCII = False  # 确保JSON响应中正确处理中文