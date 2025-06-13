from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    # Locators
    pim_menu = (By.LINK_TEXT, "PIM")
    add_button = (By.XPATH, "//button[contains(., 'Add')]")
    first_name_input = (By.NAME, "firstName")
    middle_name_input = (By.NAME, "middleName")
    last_name_input = (By.NAME, "lastName")
    employee_id_input = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
    save_button = (By.XPATH, "//button[contains(., 'Save')]")
    search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
    search_button = (By.XPATH, "//button[@type='submit']")
    employee_table = (By.XPATH, "//div[@class='oxd-table-body']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def navigate_to_pim(self):
        self._click(self.pim_menu)

    def click_add_employee(self):
        self._click(self.add_button)

    def add_employee(self, first_name, last_name, employee_id, middle_name=""):
        self._find(self.first_name_input).send_keys(first_name)
        if middle_name:
            self._find(self.middle_name_input).send_keys(middle_name)
        self._find(self.last_name_input).send_keys(last_name)
        self._find(self.employee_id_input).clear()  # limpar para garantir que o campo está vazio
        self._find(self.employee_id_input).send_keys(employee_id)
        self._click(self.save_button)

    def search_employee(self, name):
        search = self._find(self.search_input)
        search.clear()
        search.send_keys(name)
        self._click(self.search_button)
