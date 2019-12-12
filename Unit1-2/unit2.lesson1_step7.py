from selenium import webdriver
import time
import math


def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-картинку, который является изображением сундука с сокровищами
    treasure_element = browser.find_element_by_xpath('//img[@id="treasure"]')
    print(treasure_element.tag_name)
    print(treasure_element.id)
    print(treasure_element.valuex)
    # получаем значение x
    x_value = treasure_element.valuex
    # считаем формулу
    y = calc(x_value)

    # Заполняем поле с ответом
    input1 = browser.find_element_by_class_name('form-control')
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    # Выбираем radiobutton "Robots rule!"
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()

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

