from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Имя пользователя")
        self.password_input = page.get_by_role("textbox", name="Пароль")
        self.login_button = page.get_by_role("main").get_by_role("button", name="Войти")
        self.button_to_login = page.get_by_role("button", name="Вход")

    def login(self, username, password):

        self.button_to_login.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


    #     page.goto("https://demoqa.ru/qa-auto/book-store")
    # page.get_by_role("button", name="Вход").click()
    # page.get_by_role("textbox", name="Имя пользователя").click()
    # page.get_by_role("textbox", name="Пароль").click()
    # page.get_by_role("main").get_by_role("button", name="Войти").click()