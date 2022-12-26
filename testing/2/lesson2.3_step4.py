from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from math import *
import math



try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()