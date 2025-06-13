import pytest
from pages.pim_page import PIMPage
from utils.helpers import do_login  # ajuste o caminho conforme sua estrutura

def test_add_employee(driver):
    pim_page = PIMPage(driver)

    # Login
    assert do_login(driver), "Falha no login"

    # Navegar até módulo PIM
    pim_page.navigate_to_pim()

    # Clicar no botão para adicionar novo empregado
    pim_page.click_add_employee()

    # Preencher e salvar empregado
    first_name = "John"
    last_name = "Doe"
    pim_page.add_employee(first_name, last_name)

    # Validar dados do perfil automaticamente exibido
    profile_first_name = pim_page.get_profile_first_name()
    profile_last_name = pim_page.get_profile_last_name()

    assert profile_first_name == first_name, f"Esperado first name '{first_name}', mas foi '{profile_first_name}'"
    assert profile_last_name == last_name, f"Esperado last name '{last_name}', mas foi '{profile_last_name}'"
