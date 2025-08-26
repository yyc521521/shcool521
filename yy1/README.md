# 上海初升高择校平台

这是一个基于 Flask 的 Web 应用，用于帮助学生根据中考分数和区域选择合适的高中。

## 项目结构

```
.
├── app.py              # Flask 应用主文件
├── config.py           # 配置文件
├── run.py              # 应用启动文件
├── requirements.txt    # 项目依赖
├── search_logic.py     # 搜索逻辑实现
├── README.md           # 项目说明文件
├── templates/          # HTML 模板文件
│   ├── hub.html        # 首页
│   └── matches.html    # 匹配结果页
├── consultations/      # 咨询记录 JSON 文件
├── *.json              # 数据文件
```

## 宝塔面板部署指南

1. 将整个项目文件夹上传到服务器。
2. 在宝塔面板中添加 Python 项目，指向 `run.py` 文件。
3. 安装依赖：`pip install -r requirements.txt`
4. 配置项目运行端口为 5000。
5. 启动项目并配置 Nginx 反向代理。