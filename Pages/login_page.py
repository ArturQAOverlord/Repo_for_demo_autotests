from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Имя пользователя")
        self.password_input = page.get_by_role("textbox", name="Пароль")
        self.login_button = page.get_by_role("main").get_by_role("button", name="Войти")
        self.button_to_login = page.get_by_role("button", name="Вход")

    def login(self, username, password, book_list):

        self.button_to_login.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.get_by_role("button", name="Книжный магазин").click()

        for i in range(len(book_list["books"])):
            expect(self.page.get_by_role('heading', name=book_list["books"][i]["title"])).to_be_visible()