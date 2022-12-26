from math import *
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 

  link = " http://SunInJuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = x_element.text
  y = calc(x)


  # сроллим страницу вниз
  button = browser.find_element_by_tag_name("button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()

  
  input = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
  input.send_keys(y)

  checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
  checkbox.click()

  checkbox = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  checkbox.click()

  submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
  submit.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()