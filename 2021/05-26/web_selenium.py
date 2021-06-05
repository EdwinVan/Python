from selenium import webdriver
from time import sleep

dr = webdriver.Chrome("D:/MyDrivers/ChromeDriver/chromedriver.exe")
dr.get("https://www.baidu.com")
dr.maximize_window()
sleep(3)
search = dr.find_element_by_id("kw") # 定位到搜索框并赋给一个对象
search.click() #单击
search.clear() #清空
search.send_keys("selenium")#输入
dr.find_element_by_id("su").click()#单击搜索按钮
sleep(3)
if dr.title == "selenium_百度搜索":#通过窗口标题断言结果
    print("搜索成功")
else:
    print("搜索失败")
dr.quit()
