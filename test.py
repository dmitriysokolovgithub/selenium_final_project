from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
element = browser.find_element(By.XPATH, "//button[@name='registration_submit']")
element.click()
time.sleep(10)
