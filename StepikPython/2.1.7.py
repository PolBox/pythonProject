# поиск значения с помощью метода get_attribute
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.XPATH, "//div[1]/h2/img")
    treasure = x_element.get_attribute("valuex")
    x = treasure
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//div[1]/input")
    input1.send_keys(y)

    browser.find_element(By.XPATH, "//div[2]/input[1]").click()
    browser.find_element(By.XPATH, "//div[2]/input[3]").click()
    browser.find_element(By.XPATH, "//div/button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()