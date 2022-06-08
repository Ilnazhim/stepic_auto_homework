from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://front.grechka.digital/ns/data-filling.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "surname")
    input1.send_keys("Тестов")
    input2 = browser.find_element(By.ID, "name")
    input2.send_keys("Тест")
    input3 = browser.find_element(By.ID, "patronymic")
    input3.send_keys("Тестович")
    input4 = browser.find_element(By.ID, "mail")
    input4.send_keys("test@test.test")
    input6 = browser.find_element(By.ID, "date-of-birth")
    input6.send_keys("16.07.1989")
    input7 = browser.find_element(By.ID, "address")
    input7.send_keys("Московская обл. г.Химки, Уральский проезд, д.5/2 кв.159")
    input8 = browser.find_element(By.ID, "address-actual")
    input8.send_keys("Московская обл. г.Химки, Уральский проезд, д.5/2 кв.159")
    time.sleep(2)
    input9 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='__ __']")
    input9.send_keys("3709")
    input10 = browser.find_element(By.CSS_SELECTOR, "body > main:nth-child(2) > section:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > fieldset:nth-child(3) > div:nth-child(5) > div:nth-child(2) > input:nth-child(2)")
    input10.send_keys("334405")
    input11 = browser.find_element(By.CSS_SELECTOR, "body > main:nth-child(2) > section:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > fieldset:nth-child(3) > div:nth-child(5) > div:nth-child(3) > input:nth-child(2)")
    input11.send_keys("450025")
    input12 = browser.find_element(By.ID, "issued")
    input12.send_keys("27.07.2009")
    input13 = browser.find_element(By.ID, "issued-by-rf")
    input13.send_keys("ТП УФМС РОССИИ ПО КУРГАНСКОЙ ОБЛАСТИ В ЩУЧАНСКОМ РАЙОНЕ")
    browser.execute_script("window.scrollBy(0, 300);")

    check = browser.find_element(By.CSS_SELECTOR, ".main-form__formcheck:nth-child(1)")
    check.click()
    time.sleep(2)
    check = browser.find_element(By.CSS_SELECTOR, ".main-form__formcheck:nth-child(2)")
    check.click()
    time.sleep(2)


    button = browser.find_element(By.CSS_SELECTOR, ".main-form__btn")
    button.click()


    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, ".popup-success-order__text")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print(welcome_text)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Ваша заявка принята, с вами свяжется наш менеджер." == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()