import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('pageid', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_for_parametrize(browser, pageid):

    # Открываем страницу
    link = f"https://stepik.org/lesson/{pageid}/step/1/"
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока не появится нужный элемент для ввода
    WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.show-plugin textarea")))

    # Вводим правильный ответ
    answer = math.log(int(time.time()))
    input1 = browser.find_element_by_css_selector("div.show-plugin textarea")
    input1.send_keys(str(answer))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    # Дождаемся фидбека о том, что ответ правильный
    WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))

    # Проверяем, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    feedback = browser.find_element_by_class_name("smart-hints__hint")

    assert feedback.text == "Correct!", feedback.text




