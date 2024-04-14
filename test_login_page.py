from .pages.login_page import LoginPage


def test_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"  # Укажите здесь URL вашего тестируемого приложения
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
    