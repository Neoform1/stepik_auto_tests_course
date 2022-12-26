from math import *
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 

  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


 

  x_element = browser.find_element(By.ID, "treasure")
  x = x_element.get_attribute("valuex")
  y = calc(x)
  print(x)


  input = browser.find_element(By.XPATH, "/html/body/div/form/div/div/input")
  input.send_keys(y)

  checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
  checkbox.click()

  checkbox = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  checkbox.click()

  submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
  submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()