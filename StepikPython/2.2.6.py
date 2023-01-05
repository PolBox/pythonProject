# проскроллить страницу вниз
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.XPATH, "//label/span[2]")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//div[1]/input")
    input1.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")
    # button.scrollIntoView(true);
    option1 = browser.find_element(By.XPATH, "//div[2]/label")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//div[4]/label")
    option2.click()
    button = browser.find_element(By.XPATH, "//button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()