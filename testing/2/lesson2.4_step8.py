from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[2]")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    submit = browser.find_element(By.ID, "solve")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()