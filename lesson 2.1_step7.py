from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element(By.ID, "treasure")

    x_element = img.get_attribute("valuex")
    x = x_element
    y = calc(x)

    answ = browser.find_element(By.ID, "answer")
    answ.send_keys(y)
    time.sleep(1)
    che = browser.find_element(By.ID, "robotCheckbox")
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
