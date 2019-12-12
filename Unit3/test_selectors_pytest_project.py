from selenium import webdriver
import time
import unittest


# function to register on the specified URL
def selectors(page_url):
    try:
        browser = webdriver.Chrome()
        # open the link in Browser
        browser.get(page_url)

        # Fill all the input fields
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("abc@abc.ru")
        input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
        input4.send_keys("+1-123-123-12-12")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
        input5.send_keys("Home")

        # Click Submit button
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Wait till page has loaded and check that got registered
        time.sleep(1)

        # Find element containing the required text
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # Write text from welcome_text_elt into variable welcome_text
        welcome_text = welcome_text_elt.text

        # Return variable welcome_text value
        return welcome_text

    finally:
        # Wait to visually check the script results
        time.sleep(5)
        # Close Browser
        browser.quit()


# test #1: try registration1.html
def test_selector1():
    # set URL to open
    page_url = "http://suninjuly.github.io/registration1.html"
    # Set the expected text
    successful_text = "Congratulations! You have successfully registered!"
    # Verify that the text returned by function selector is the expected
    assert selectors(page_url) == successful_text, "Should be successful registration"


# test #2: try registration2.html
def test_selector2():
    # set URL to open
    page_url = "http://suninjuly.github.io/registration2.html"
    # Set the expected text
    successful_text = "Congratulations! You have successfully registered!"
    # Verify that the text returned by function selector is the expected
    assert selectors(page_url) == successful_text, "Should be successful registration"


if __name__ == "__main__":
    unittest.main()





