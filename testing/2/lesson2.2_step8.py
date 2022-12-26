from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    first_name.send_keys("Tyoma")
    last_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    last_name.send_keys("Z")
    Email = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    Email.send_keys('tyoma@z.com')


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(file_path)
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)
    
    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()