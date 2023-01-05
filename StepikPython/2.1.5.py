# решение формулы и вставка результата для подтверждения
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.XPATH, "//div[1]/label/span[2]")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//div[1]/input")
    input1.send_keys(y)

    option1 = browser.find_element(By.XPATH, "//div[2]/label")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//div[4]/label")
    option2.click()
    button = browser.find_element(By.XPATH, "//form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()