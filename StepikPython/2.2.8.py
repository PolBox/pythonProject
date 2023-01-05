# загрузка файла из указанного пути
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(By.XPATH, "//div[1]/input[1]").send_keys("Ivan")
    browser.find_element(By.XPATH, "//div[1]/input[2]").send_keys("Ivanov")
    browser.find_element(By.XPATH, "//div[1]/input[3]").send_keys("Ivanov")
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, "//form/input")
    element.send_keys(file_path)
    browser.find_element(By.XPATH, "//button").click()
finally:
    time.sleep(5)
    browser.quit()