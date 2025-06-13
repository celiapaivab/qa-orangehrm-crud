from pages.login_page import LoginPage

def do_login(driver, username="Admin", password="admin123"):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.submit()
    return login_page.is_dashboard_displayed()
