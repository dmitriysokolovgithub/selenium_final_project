from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    TOP_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
    RU_BASKET_EMPTY_TEXT = (By.XPATH,
                            "//div[@class='content']/*/p[contains(text(), 'Ваша корзина пуста')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    REG_SUCCESS_ALERT = (By.CSS_SELECTOR, ".icon-ok-sign")


class ProductPageLocators:
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_FROM_ALERT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    CART_SUM_FROM_ALERT = (By.XPATH,
                           "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/div/p/strong")
    TITLE_FROM_CART = (By.XPATH, "//h1")
    CART_SUM_FROM_CART = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[1]")
    CART_SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
