from selenium import webdriver
import time
import math


def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.trollface.btn")
    button.click()

    # Переключаемся на новую вкладку
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)

    # Находим поле со значением x
    x_element = browser.find_element_by_id('input_value')
    # получаем значение x
    x_value = x_element.text
    # считаем формулу
    y = calc(x_value)

    # Заполняем поле с ответом
    input = browser.find_element_by_class_name('form-control')
    input.send_keys(y)

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
