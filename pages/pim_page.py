from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    PIM_MENU = (By.LINK_TEXT, "PIM")
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space[type='submit']")
    PROFILE_FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input.orangehrm-firstname")
    PROFILE_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input.orangehrm-lastname")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def navigate_to_pim(self):
        self._click(self.PIM_MENU)

    def click_add_employee(self):
        self._click(self.ADD_BUTTON)

    def add_employee(self, first_name, last_name):
        first_name_field = self._find(self.FIRST_NAME_INPUT)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self._find(self.LAST_NAME_INPUT)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        self._click(self.SAVE_BUTTON)

    def get_profile_first_name(self):
        element = self._find(self.PROFILE_FIRST_NAME_INPUT)
        return element.get_attribute("value").strip()

    def get_profile_last_name(self):
        element = self._find(self.PROFILE_LAST_NAME_INPUT)
        return element.get_attribute("value").strip()
