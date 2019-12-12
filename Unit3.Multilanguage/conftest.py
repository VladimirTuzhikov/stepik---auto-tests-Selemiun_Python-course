import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help="Set language")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def langopt(request):
    return request.config.getoption("--language")
