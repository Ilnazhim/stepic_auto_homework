from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answ = browser.find_element(By.ID, "answer")
    answ.send_keys(y)
    time.sleep(1)
    che = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    che.click()
    time.sleep(1)
    rad = browser.find_element(By.ID, "robotsRule")
    rad.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
