from selenium import webdriver
from selenium.webdriver.common.by import By
# 打开网页
driver = webdriver.Chrome()
try:
    driver.get("https://www.baidu.com")
    title = driver.title
    print(title)
    input_box = driver.find_element(By.ID, 'kw')
    input_box.send_keys('Selenium helloWord')
    # 定位查询按钮并点击
    search_button = driver.find_element(By.ID, 'su')
    search_button.click()
    driver.implicitly_wait(1000)
    input("按 Enter 键关闭浏览器...")
finally:
    # 关闭浏览器
    driver.quit()