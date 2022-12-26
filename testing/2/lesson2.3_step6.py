from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    flying_button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    flying_button.click()


    # swithing to a new tab
    new_window = browser.window_handles[1]
    print(new_window)
    first_window = browser.window_handles[0]
    print(first_window)
    browser.switch_to.window(new_window)



    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[2]")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)


    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()