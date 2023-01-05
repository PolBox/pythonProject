# ожидание необходимого текста на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[1]/h5[2]"), "100")
    )
    button = browser.find_element(By.XPATH, "//div/div/div/button")
    button.click()
    # assert "successful" in message.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.XPATH, "//label/span[2]")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//div/div/input")
    input1.send_keys(y)
    button1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    # actions = ActionChains(browser)
    # actions.move_to_element(target)
    button1.click()
finally:
    print(browser.switch_to.alert.text)
    # time.sleep(5)
    browser.quit()