# выпадающий список
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.XPATH, "//h2/span[2]")
    b = browser.find_element(By.XPATH, "//h2/span[4]")
    z = str(int(a) + int(b))
    # x = x_element.text
    # y = str(sum)

    select = Select(browser.find_element(By.XPATH, "//div/select"))
    select.select_by_value(40)  # ищем элемент с текстом "Python"

    # browser.find_element(By.XPATH, "//div[2]/input[1]").click()
    # browser.find_element(By.XPATH, "//div[2]/input[3]").click()
    # browser.find_element(By.XPATH, "//div/button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()