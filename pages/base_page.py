from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def are_elements_text_equal(self, first_elem_locator, second_elem_locator):
        try:
            first_element_text = self.browser.find_element(*first_elem_locator).text
            second_element_text = self.browser.find_element(*second_elem_locator).text
            print(f"first_element_text = '{first_element_text}', second_element_text = '{second_element_text}'")
        except NoSuchElementException:
            return False
        return first_element_text == second_element_text
