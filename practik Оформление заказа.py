from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://novascreen.ru/analyzes/koagulogramma-rasshirennaya-kompleks/"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.cart-add")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.js-office-button")
    button.click()
    button = browser.find_element_by_id("bx_basketFKauiI")
    button.click()
    button = browser.find_element_by_css_selector("a.cart-section__aside-button")
    button.click()
    time.sleep(1)
    input1 = browser.find_element(By.ID, "ORDER_PROP_2")
    input1.send_keys("Тестов")
    input2 = browser.find_element(By.ID, "ORDER_PROP_9")
    input2.send_keys("Тест")
    input3 = browser.find_element(By.ID, "ORDER_PROP_10")
    input3.send_keys("Тестович")
    input4 = browser.find_element(By.ID, "ORDER_PROP_3")
    input4.send_keys("16.07.1989")
    input5 = browser.find_element(By.ID, "ORDER_PROP_4")
    input5.send_keys("9511299052")
    input6 = browser.find_element(By.ID, "ORDER_PROP_5")
    input6.send_keys("test@test.test")
    input7 = browser.find_element(By.ID, "ORDER_PROP_50")
    input7.send_keys("07.06.2022")
    input8 = browser.find_element(By.ID, "ORDER_PROP_51")
    input8.send_keys("1230")
    input9 = browser.find_element(By.ID, "ORDER_PROP_52")
    input9.send_keys("Московская обл. г.Химки, Уральский проезд, д.5/2 кв.159")
    browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)

    check = browser.find_element(By.CSS_SELECTOR, ".main-form__agree-block:nth-child(2)")
    check.click()
    time.sleep(3)
    check = browser.find_element(By.CSS_SELECTOR, "[for='agree']")
    check.click()
    time.sleep(10)

    button = browser.find_element(By.ID, "ORDER_CONFIRM_BUTTON")
    button.click()

    # Отправляем заполненную форму
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()