from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def sum(x, y):
        return str(int(x) + int(y))

    x_element = browser.find_element(By.XPATH, "/html/body/div/form/h2/span[2]")
    x = x_element.text

    y_element = browser.find_element(By.XPATH, "/html/body/div/form/h2/span[4]")
    y = y_element.text

    z = sum(x, y)


    browser.find_element(By.TAG_NAME, "select").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z) 

    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit.click()


finally:
    print(z)

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    
    # закрываем браузер после всех манипуляций
    browser.quit()