# -*- coding: utf-8 -*-
import time
from selenium import webdriver

url = 'http://www.baidu.com'

# 创建一个浏览器对象
dr = webdriver.Chrome()
# dr = webdriver.PhantomJS()

# 访问url
dr.get(url)

# 定位元素节点的8中方法
'''
使用id值定位
el = driver.find_element_by_id				

使用xpath定位
el = driver.find_elements_by_xpath			

使用标签名定位
el = driver.find_elements_by_tag_name		

使用文本定位, 注意:文本需要含有链接
el = driver.find_elements_by_link_text 		

使用部分文本定位, 注意:文本需要含有链接
el = driver.find_elements_by_partial_link_text 	

使用name属性值定位
el = driver.find_elements_by_name 			

使用class属性值定位
el = driver.find_elements_by_class_name 		

使用css选择器定位
el = driver.find_elements_by_css_selector		

'''
# 1. 使用id值定位
el = dr.find_element_by_id('kw')  # 定位到百度搜索框这个节点
el1 = dr.find_element_by_id('su')  # 定位到百度一下这个提交搜索的按钮节点

# 获取搜索框中的属性的值
# print(el.get_attribute('name'))
# 向搜索框中输入搜索值
el.send_keys('熊猫直播')
# 提交搜索
# el1.click()

# 使用文本定位
# el = dr.find_element_by_link_text('hao123')
# el.click()
# el = dr.find_element_by_partial_link_text('斗鱼')
# el = dr.find_element_by_id('search-input')
# el.send_keys('熊猫直播')
# el = dr.find_element_by_xpath('//*[@id="search-form"]/div[2]/input')
# el.click()
time.sleep(2)
print('start')
el = dr.find_element_by_xpath(r'//*[@id="9"]/h3/a')
print(el)
url = el.get_attribute('href')
print(url)

dr.get(url)
# el.click()
# dr.close()


