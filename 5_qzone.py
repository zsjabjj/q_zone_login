# -*- coding: utf-8 -*-
from selenium import webdriver

url = 'https://qzone.qq.com/'

dr = webdriver.Chrome()

# 访问url
dr.get(url)

# 因为QQ登录是在一个框架中又有一个框架
# 所以需要先进框架, 再定位节点元素
# 进入框架有两种方法
# 1. 通过框架id进入
# dr.switch_to.frame('login_frame')

# 2. 通过节点定位
el_frame = dr.find_element_by_xpath('//*[@id="login_frame"]')
dr.switch_to.frame(el_frame)

# 定位'账号登录'节点
# el = dr.find_element_by_xpath('//*[@id="switcher_plogin"]')
el = dr.find_element_by_id('switcher_plogin')
el.click()
# dr.save_screenshot('qzone.png')

# 输入账号和密码
el_user = dr.find_element_by_id('u')
el_user.send_keys('2634809316')
el_pwd = dr.find_element_by_id('p')
el_pwd.send_keys('461324karura')
dr.implicitly_wait(10)
el_btn = dr.find_element_by_id('login_button')
el_btn.click()