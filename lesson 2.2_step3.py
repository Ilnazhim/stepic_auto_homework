from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])


try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)



    at = browser.find_element(By.ID, "num1")
    a = at.text
    bt = browser.find_element(By.ID, "num2")
    b = bt.text

    sum=(int(a)+int(b))
    print(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(sum))
        #x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    #x = x_element.text
    #y = calc(x)

    #print(int(a)+int(b))
    #(a, b) = input().split()
   # print(int(a) + int(b))

    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value("1")  # ищем элемент с текстом "Python"
    #select.select_by_value(value=str(summa))
    #img = browser.find_element(By.ID, "treasure")

    #x_element = img.get_attribute("valuex")
    #x = x_element
    #y = calc(x)
   # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    #browser.execute_script("document.title='Script executing';")
    #browser.execute_script("alert('Robots at work');")


    #answ = browser.find_element(By.ID, "answer")
    #answ.send_keys(y)
    #time.sleep(1)
    #che = browser.find_element(By.ID, "robotCheckbox")
    #che.click()
    time.sleep(1)
   # rad = browser.find_element(By.ID, "robotsRule")
   # rad.click()
    #time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
