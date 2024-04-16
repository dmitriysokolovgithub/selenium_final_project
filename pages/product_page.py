from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        link.click()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON), "Cart button is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_correct_title(self):
        assert self.are_elements_text_equal(ProductPageLocators.TITLE_FROM_ALERT,
                                            ProductPageLocators.TITLE_FROM_CART), "titles aren't equal"

    def should_be_correct_sum(self):
        assert self.are_elements_text_equal(ProductPageLocators.CART_SUM_FROM_ALERT,
                                            ProductPageLocators.CART_SUM_FROM_CART), "prices aren't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CART_SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.CART_SUCCESS_ALERT), \
            "Success message is disappeared"


