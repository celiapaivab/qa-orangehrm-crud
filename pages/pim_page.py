from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException




class PIMPage:
    # Localizadores adicionar funcionário
    PIM_MENU = (By.LINK_TEXT, "PIM")
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space[type='submit']")
    PROFILE_FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input.orangehrm-firstname")
    PROFILE_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input.orangehrm-lastname")
    # Localizadores pesquisar funcionário
    EMPLOYEE_LIST_TAB = (By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab')]//a[text()='Employee List']")
    SEARCH_EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(., 'Search')]")
    TABLE_CONTAINER = (By.CSS_SELECTOR, "div.oxd-table-body")
    # Localizadores editar funcionário
    PERSONAL_DETAILS_TITLE = (By.XPATH, "//h6[contains(., 'Personal Details')]")
    SAVE_EDIT_BUTTON = "//button[@type='submit' and contains(normalize-space(.), 'Save')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Métodos adicionar funcionário
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

    # Métodos pesquisar funcionário
    def navigate_to_employee_list(self):
        self._click(self.EMPLOYEE_LIST_TAB)
        self._find(self.SEARCH_EMPLOYEE_NAME_INPUT)

    def search_employee_by_name(self, full_name):
        search_input = self._find(self.SEARCH_EMPLOYEE_NAME_INPUT)
        search_input.clear()
        search_input.send_keys(full_name)
        self._click(self.SEARCH_BUTTON)
        # Espera pelo container da tabela
        self.wait.until(EC.visibility_of_element_located(self.TABLE_CONTAINER))

    def is_employee_in_list(self, first_name, last_name):
        xpath = (
            f"//div[contains(@class, 'oxd-table-row') and "
            f"contains(translate(.//div[@role='cell'][3]/div/text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{first_name.lower()}') and "
            f"contains(translate(.//div[@role='cell'][4]/div/text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{last_name.lower()}')]"
        )
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            print("Funcionário não encontrado na lista.")
            return False

    # Métodos editar funcionário
    def click_edit_employee(self, first_name, last_name):
        row_xpath = (
            f"//div[contains(@class, 'oxd-table-row') and "
            f"contains(translate(.//div[@role='cell'][3]/div/text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{first_name.lower()}') and "
            f"contains(translate(.//div[@role='cell'][4]/div/text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{last_name.lower()}')]"
            f"//div[@class='oxd-table-cell-actions']/button[1]"
        )
        self._click((By.XPATH, row_xpath))

    def is_personal_details_page_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PERSONAL_DETAILS_TITLE))
            return True
        except TimeoutException:
            return False

    def edit_employee_name(self, first_name, last_name):
        first_name_field = self.driver.find_element(By.NAME, "firstName")
        first_name_field.clear()
        # envia backspace para garantir limpeza
        for _ in range(10):
            first_name_field.send_keys(Keys.BACKSPACE)
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.NAME, "lastName")
        last_name_field.clear()
        for _ in range(10):
            last_name_field.send_keys(Keys.BACKSPACE)
        last_name_field.send_keys(last_name)

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_EDIT_BUTTON))
        )
        save_button.click()

