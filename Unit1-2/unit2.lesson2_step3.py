from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим поле со значением первого слагаемого
    x_element = browser.find_element_by_id('num1')
    # получаем значение x
    x_value = x_element.text

    # Находим поле со значением второго слагаемого
    y_element = browser.find_element_by_id('num2')
    # получаем значение y
    y_value = y_element.text

    # считаем сумму
    z = int(x_value) + int(y_value)

    # Заполняем поле с ответом
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(z))  # ищем элемент со значением z

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

