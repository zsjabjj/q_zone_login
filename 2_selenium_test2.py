# -*- coding: utf-8 -*-
from selenium import webdriver

# dr = webdriver.PhantomJS(executable_path=r"H:\ProgramData\phantomjs\bin\phantomjs.exe")
# 将phantomjs放在system32中就OK了
dr = webdriver.PhantomJS()
# dr = webdriver.Chrome()

# dr.maximize_window()
# 发送url请求
dr.get('http://www.baidu.com')

# 保存屏幕截图
# dr.save_screenshot('baidu.png')

# 获取源码
# print(dr.page_source)

# 获取浏览器中存储的cookies, 如果要构建cookie, 取出name和value, 构建字典
# print(dr.get_cookies())

# 查看当前url
# print(dr.current_url)

# 查看当前标签的标题
# print(dr.title)

# 元素定位, 此处只能定位到节点, 不能获取到值, 值用其他方法取, 例如data.text 获取text值
data = dr.find_element_by_xpath('//*[@id="u1"]/a[1]')
# print(data)  # 新闻对应的a标签

# 点击新闻的a标签
data.click()
print('click')
# 直接可以保存, 生成图片, 图片是整个网页
# dr.get_screenshot_as_file('news1.png')

# save_screenshot()也是如此, 不过是当前窗口的截图
# dr.save_screenshot('news.png')

# 获取到整个网页图片的源码, 然后将源码写入, 保存成图片
png = dr.get_screenshot_as_png()
with open('news2.png', 'wb') as f:
    f.write(png)
print('save')
dr.close()

