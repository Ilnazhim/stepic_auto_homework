from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import  time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(y)

    button = browser.find_element_by_css_selector (".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()