# 简介

> 基于selenium的简单的自动化回复Demo
>
> Python 版本3.5
>
> ChromeDriver 版本 89.0.4389.23 需要和本机的Chrome版本相同,下载驱动后放置seleniumDome目录下

## 快速开始

### 安装selenium包

```shell script
pip3 install selenium -i https://mirrors.aliyun.com/pypi/simple/
```

### 初始化cookie

```shell script
// 初始化cookie
// 第一次登录需要自行扫码登录,保存cookie到本地
python spider/__init__.py
```

### 回复测试
```shell script
python spider/reply.py
```