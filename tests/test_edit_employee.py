import time
from pages.pim_page import PIMPage
from utils.helpers import do_login

EMP_FIRST_NAME = "Ana"
EMP_LAST_NAME = "Silva"
EMP_FULL_NAME = f"{EMP_FIRST_NAME} {EMP_LAST_NAME}"
NEW_FIRST_NAME = "Ana Maria"
NEW_LAST_NAME = "Souza"
NEW_FULL_NAME = f"{NEW_FIRST_NAME} {NEW_LAST_NAME}"

def test_edit_employee(driver):
    pim_page = PIMPage(driver)

    # Login
    do_login(driver)

    # Adiciona funcionário
    pim_page.navigate_to_pim()
    time.sleep(1)
    pim_page.click_add_employee()
    time.sleep(1)
    pim_page.add_employee(EMP_FIRST_NAME, EMP_LAST_NAME)
    time.sleep(1)
    assert pim_page.get_profile_first_name() == EMP_FIRST_NAME, "Primeiro nome incorreto após cadastro"
    assert pim_page.get_profile_last_name() == EMP_LAST_NAME, "Último nome incorreto após cadastro"

    # Navega até lista e pesquisa
    pim_page.navigate_to_employee_list()
    time.sleep(1)
    pim_page.search_employee_by_name(EMP_FULL_NAME)
    time.sleep(1)

    # Clica no botão de editar
    pim_page.click_edit_employee(EMP_FIRST_NAME, EMP_LAST_NAME)
    time.sleep(1)
    assert pim_page.is_personal_details_page_displayed(), "Página de detalhes pessoais não exibida"

    # Edita nome e sobrenome
    pim_page.edit_employee_name(NEW_FIRST_NAME, NEW_LAST_NAME)
    time.sleep(3)
    assert pim_page.get_profile_first_name() == NEW_FIRST_NAME, "Primeiro nome não atualizado na página de detalhes"
    assert pim_page.get_profile_last_name() == NEW_LAST_NAME, "Último nome não atualizado na página de detalhes"

    # Verifica na lista
    pim_page.navigate_to_employee_list()
    time.sleep(1)
    pim_page.search_employee_by_name(NEW_FULL_NAME)
    time.sleep(3)
    assert pim_page.is_employee_in_list(NEW_FIRST_NAME, NEW_LAST_NAME), "Edição não refletida na lista"
