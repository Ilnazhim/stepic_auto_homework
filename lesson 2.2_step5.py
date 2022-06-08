from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import  time
from selenium.webdriver.chrome.options import Options
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    browser.execute_script("window.scrollBy(0, 100);")


    rad = browser.find_element_by_id("robotsRule")
    rad.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()