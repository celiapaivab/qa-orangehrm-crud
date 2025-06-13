from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com"
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.oxd-button[type='submit']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def open(self):
        self.driver.get(self.URL)

    def fill_username(self, username):
        username_field = self._find(self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)

    def fill_password(self, password):
        password_field = self._find(self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def submit(self):
        self._click(self.SUBMIT_BUTTON)

    def is_dashboard_displayed(self):
        try:
            self._find(self.DASHBOARD_HEADER)
            return True
        except:
            return False
