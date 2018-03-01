# -*- coding: utf-8 -*-
import time
from selenium import webdriver

dr = webdriver.Chrome()
# 打印所有dr中的方法
print(dir(dr))
# 打开窗口, 最大化显示

dr.get('http://www.baidu.com')
dr.maximize_window()

time.sleep(5)
dr.close()