# переход на новую вкладку
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    # browser.get("http://suninjuly.github.io/redirect_accept.html")  можно писать ссылку так
    browser.find_element(By.XPATH, "//button").click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.XPATH, "//label/span[2]")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//div/input")
    input1.send_keys(y)
    browser.find_element(By.XPATH, "//button").click()
finally:
    print(browser.switch_to.alert.text)
    # time.sleep(10)
    browser.quit()