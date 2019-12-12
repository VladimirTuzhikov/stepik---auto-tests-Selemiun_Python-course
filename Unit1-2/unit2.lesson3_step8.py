from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена дома не уменьшится до $100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем на кнопку "Book"
    book = browser.find_element_by_id("book")
    book.click()
    # проскролим вниз
    browser.execute_script("return arguments[0].scrollIntoView(true);", book)

    # Находим поле со значением x
    x_element = browser.find_element_by_id('input_value')
    # получаем значение x
    x_value = x_element.text
    print(x_value)
    # считаем формулу
    y = calc(x_value)

    # Заполняем поле с ответом
    input = browser.find_element_by_class_name('form-control')
    input.send_keys(y)

    # Отправляем заполненную форму
    solve = browser.find_element_by_id("solve")
    solve.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
