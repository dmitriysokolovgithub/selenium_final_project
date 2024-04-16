from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.TOP_BASKET_LINK)
        link.click()

    def should_not_be_products(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS)

    def should_be_text_about_empty_basket(self):
        self.is_element_present(*BasketPageLocators.RU_BASKET_EMPTY_TEXT)