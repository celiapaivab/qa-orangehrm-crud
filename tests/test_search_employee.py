import time

from pages.login_page import LoginPage
from pages.pim_page import PIMPage

# Constantes para os dados do empregado
EMP_FIRST_NAME = "Ana"
EMP_LAST_NAME = "Silva"
EMP_FULL_NAME = f"{EMP_FIRST_NAME} {EMP_LAST_NAME}"

def test_search_employee(driver):
    login_page = LoginPage(driver)
    pim_page = PIMPage(driver)

    login_page.open()
    login_page.fill_username("Admin")
    login_page.fill_password("admin123")
    login_page.submit()
    assert login_page.is_dashboard_displayed(), "Falha no login"

    pim_page.navigate_to_pim()
    pim_page.click_add_employee()
    pim_page.add_employee(EMP_FIRST_NAME, EMP_LAST_NAME)
    assert pim_page.get_profile_first_name() == EMP_FIRST_NAME, "Primeiro nome incorreto após cadastro"
    assert pim_page.get_profile_last_name() == EMP_LAST_NAME, "Último nome incorreto após cadastro"
    time.sleep(1)

    pim_page.navigate_to_employee_list()
    time.sleep(1)
    pim_page.search_employee_by_name(EMP_FULL_NAME)
    time.sleep(1)
    assert pim_page.is_employee_in_list(EMP_FIRST_NAME, EMP_LAST_NAME), "Empregado não encontrado na lista"
