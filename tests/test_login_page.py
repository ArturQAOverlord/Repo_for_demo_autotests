from Pages.login_page import LoginPage


def test_login(page, user):
    login_page = LoginPage(page)

    page.goto("https://demoqa.ru/qa-auto/book-store")

    login_page.login(
        user["username"],
        user["password"]
    )

    