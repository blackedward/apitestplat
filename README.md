## KiwiTest平台服务端代码

### 简介

_本工程是kiwitest平台的后端代码，基于flask框架简单实现，目前支持http、socket协议接口测试，其他增值功能包括：单用例、多用例串行、用例返回数据提取、预置SQL执行等功能_

### 项目结构

```入口文件：run.py，用blueprint实现模块化管理 config.py为配置文件 sql和redis配置在此文件中，不过目前没有使用到redis```

```目前所有挂载的blueprint都在app目录下，分为三个部分：user、project、interfacecase```

```
├── app
│   ├── __init__.py #SQLAlchemy 初始化     
│   ├── interfacecase # 接口用例模块
│   ├── projects # 项目模块
│   ├── users # 用户模块 
│   ├── models.py # 所有数据库实例维护文件
   
```

``` common目录下存放了最核心的逻辑处理代码，几个重点文件说明如下：```

```
├── common
│   ├── exesql.py # SQL执行 
│   ├── executehandler.py #  **用例执行核心代码，包括http、socket协议的执行**
│   ├── AnalysisPB.py #  一键执行PB协议的核心代码
```

```lib目录下存放了一些公共的方法，不是太重要，主要是一些被依赖的工具类方法```

```proto目录下是 测试socket协议的proto文件，如有新增的需要及时更新```

```sql目录下DDL 是数据库表结构```

### 部署情况

```目前部署在阿里云服务器上，gunicorn+flask+supervisor的方式在部署，不过目前supervisor没有激活，容器地址 47.242.225.5端口 5000```

```部署方式：root用户下进入项目根目录 /root/code/kiwitest ，执行命令 gunicorn -w5 -b0.0.0.0:5000 run:app  不要用文件方式启动，否则会报错```
```本地开发测试可以直接执行run.py启动 ```