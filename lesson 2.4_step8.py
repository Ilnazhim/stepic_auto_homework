from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 12).until(
             EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

#assert "successful" in message.text
finally:
    time.sleep(10)
    browser.quit()