# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 下午3:06
# @Software: PyCharm
from PIL import Image
import requests,chardet,psutil
r = requests.get('https://www.baidu.com/')
print(r.status_code)
print(r.text)
print(r.encoding)
# print(r.json())
# print(chardet.detect())
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.pids())
print(psutil.test())