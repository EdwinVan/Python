# 网页测试
# 目标网页：https://www.lagou.com/zhaopin/ 
# 完成重庆市计算机行业工作的查找，月薪5k-10k 
# 要求调用到的方法： 1.下拉菜单的选择； 2.xpath定位

from selenium import webdriver
from time import sleep
dr= webdriver.Chrome()
dr.get('https://www.lagou.com/zhaopin/')
dr.maximize_window()
sleep(3)
search = dr.find_element_by_id("keyword")
search.click()
search.clear()
search.send_keys("重庆市计算机行业")
dr.find_element_by_id("submit").click()
sleep(3)
windows = dr.window_handles
dr.switch_to.window(windows[-1])
sleep(1)
dr.execute_script('window.scrollBy(0,220)')
dr.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/ul[2]/li/div[2]/div/i").click()
sleep(5)
dr.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/ul[2]/li/div[2]/div/ul/li[4]").click()
sleep(2)
dr.execute_script('window.scrollBy(0,-90)')
sleep(10)
print("测试成功")
dr.quit()
