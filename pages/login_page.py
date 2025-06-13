from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    dashboard_title = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def fill_username(self, username):
        elem = self._find(self.username_input)
        elem.clear()
        elem.send_keys(username)

    def fill_password(self, password):
        elem = self._find(self.password_input)
        elem.clear()
        elem.send_keys(password)

    def submit(self):
        self._find(self.login_button).click()

    def is_dashboard_displayed(self):
        try:
            self._find(self.dashboard_title)
            return True
        except:
            return False
