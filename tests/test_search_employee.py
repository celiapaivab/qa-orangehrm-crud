import time
from pages.pim_page import PIMPage
from utils.helpers import do_login

EMP_FIRST_NAME = "Ana"
EMP_LAST_NAME = "Silva"
EMP_FULL_NAME = f"{EMP_FIRST_NAME} {EMP_LAST_NAME}"

def test_search_employee(driver):
    pim_page = PIMPage(driver)

    do_login(driver)

    pim_page.navigate_to_pim()
    time.sleep(1)

    pim_page.click_add_employee()
    time.sleep(1)

    pim_page.add_employee(EMP_FIRST_NAME, EMP_LAST_NAME)
    time.sleep(1)

    assert pim_page.get_profile_first_name() == EMP_FIRST_NAME, "Primeiro nome incorreto após cadastro"
    assert pim_page.get_profile_last_name() == EMP_LAST_NAME, "Último nome incorreto após cadastro"

    pim_page.navigate_to_employee_list()
    time.sleep(1)

    pim_page.search_employee_by_name(EMP_FULL_NAME)
    time.sleep(1)

    assert pim_page.is_employee_in_list(EMP_FIRST_NAME, EMP_LAST_NAME), "Empregado não encontrado na lista"
