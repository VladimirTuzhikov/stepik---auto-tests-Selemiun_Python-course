import time


def test_multilanguage_interface(browser, langopt):
    # Открываем страницу
    link = f"http://selenium1py.pythonanywhere.com/{langopt}/catalogue/coders-at-work_207/"
    browser.get(link)

    # Ожидание чтобы визуально оценить правильный язык на кпоке "Добавить в крозину"
    time.sleep(15)

    # Проверям, что кнопка "Добвать в корзину" находится на странице
    assert browser.find_element_by_css_selector("#add_to_basket_form button"), "Add to bucket button must be located"

