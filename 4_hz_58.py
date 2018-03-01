# -*- coding: utf-8 -*-
import json
import time
from selenium import webdriver

url = 'http://hz.58.com/'

# dr = webdriver.Chrome()
dr = webdriver.PhantomJS()

dr.implicitly_wait(10)

dr.get(url)

'''
所谓"弹窗",并不是指前面的alert一类由js产生的对话框, 
而是指打开一个新链接(target=”_blank”)时,产生的新的浏览器窗口.

这时需要用到的函数是switch_to.window()

这个函数接受两种参数.一个就是窗口句柄(可以通过window_handles属性获得),
另一个就是新打开窗口名称(即a标签中target属性的值,不能是_blank等关键字)

窗口句柄: --->句柄是一种内部代码，通过它能引用受系统控制的特殊元素，如窗口、位图、图标、内存块、光标、字体、菜单等
在windows中，句柄是和对象一一对应的32位无符号整数值。
窗口句柄列表-->
['CDwindow-(775220D561F8C369CDA934F36AEEA922)', 'CDwindow-(875F2B39227FE8CF8B2BE6222F219219)']
对象可以映射到唯一的句柄，句柄也可以映射到唯一的对象。
'''

# 获取当前页面url
print(dr.current_url)
# 获取所有的窗口的列表
print(dr.window_handles)

# 模拟点击房屋出租
el = dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/em[1]/a')
# print(dir(el))
el.click()
print(dr.window_handles)
# 切换窗口
# dr.implicitly_wait(10)
dr.switch_to.window(dr.window_handles[-1])
print(dr.current_url)
# 获取当前窗口句柄
print(dr.current_window_handle)
# dr.implicitly_wait(10)

# time.sleep(5)
print('start xpath')
# 选择一室, 整租
# room_list = list()
print('room')
one_room = dr.find_element_by_xpath('//*[@id="secitem-room"]/a[2]')
one_room.click()
# dr.implicitly_wait(10)
# room_list.append(one_room)
print('house')
full_house = dr.find_element_by_xpath('//*[@id="secitem-type"]/a[2]')
full_house.click()
# room_list.append(full_house)
# print(room_list)
# for room in room_list:
#     print(room)
#     room.click()
#     print('click')
#     dr.implicitly_wait(10)
#     print('-' * 30)


# dr.implicitly_wait(10)
# 获取当前页的数据
node_list = dr.find_elements_by_xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a[1]')
price_list = dr.find_elements_by_xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[3]/div[2]/b')
# //*[@id="secitem-room"]/a[2]  一室
# //*[@id="secitem-type"]/a[2]  整租
zufang_list = list()
for i in range(0, len(node_list)):
    temp = dict()
    temp['title'] = node_list[i].text
    temp['link'] = node_list[i].get_attribute('href')
    temp['price'] = price_list[i].text + '元/月'
    zufang_list.append(temp)
print(zufang_list)
    # print(i)
    # print(node_list[i].text, node_list[i].get_attribute('href'))
    # print(price_list[i].text)
f = open('zufang.json', 'w', encoding='UTF-8')
for zufang in zufang_list:
    print(zufang)
    zufang_str = json.dumps(zufang, ensure_ascii=False) + ',\n'
    f.write(zufang_str)
f.close()
# dr.implicitly_wait(10)
# dr.close()
