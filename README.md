# 软件测试与质量保证

## Commission后台

使用`pip`安装相关依赖：

    (sudo) pip install -r requirements.txt

使用`gunicorn`开启后台：

    gunicorn -c gunicorn.ini newspaper:app

在`Pycharm`下运行`test/main.py`即可运行测试脚本。    
如果不使用IDE，直接用Python命令运行，则会因为`Commission`的路径无法找到而出现问题。             
此时可以将本项目根路径添加到`os.path`中，如果不会请自行Google之。        

### 测试用例

本课程实验的目的是利用所学的黑盒测试与白盒测试知识，对代码进行测试。              
本实验后台部分使用`unittest`进行测试，前端和后台作为两个独立模块分别测试。
