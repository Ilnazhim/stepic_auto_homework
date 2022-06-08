from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://novascreen.ru/home-visit/"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".order-card_active .order-card__popup-button")
    button.click()
    time.sleep(1)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "fio")
    input1.send_keys("Тест Тестов Тестович")
    time.sleep(1)
    input2 = browser.find_element(By.ID, "date-of-birth")
    input2.send_keys("16.07.89")
    time.sleep(1)
    input3 = browser.find_element(By.ID, "phone")
    input3.send_keys("9511299052")
    time.sleep(1)
    input4 = browser.find_element(By.ID, "mail")
    input4.send_keys("test@test.test")
    time.sleep(1)
    input5 = browser.find_element(By.ID, "address")
    input5.send_keys("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    time.sleep(1)
    input6 = browser.find_element(By.ID, "date-of-arrival")
    input6.send_keys("03.06.2022")
    time.sleep(1)
    check = browser.find_element(By.CSS_SELECTOR, "[for='agree']")
    check.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.feedback-popup__submit-button")
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
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()