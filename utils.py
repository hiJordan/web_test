from jinja2 import Environment, FileSystemLoader
import os.path
import time
import json


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    date_format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(date_format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
