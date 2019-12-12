from selenium import webdriver
import time
import math


def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Находим поле со значением x
    x_element = browser.find_element_by_id('input_value')
    # получаем значение x
    x_value = x_element.text
    # считаем формулу
    y = calc(x_value)

    # Заполняем поле с ответом
    input1 = browser.find_element_by_class_name('form-control')
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
