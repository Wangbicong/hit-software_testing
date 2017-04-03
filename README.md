# 软件测试与质量保证

## Commission后台

使用`pip`安装相关依赖：

    (sudo) pip install -r requirements.txt

使用`gunicorn`开启后台：

    gunicorn -c gunicorn.ini newspaper:app
