import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

def test_add_employee(driver):
    login_page = LoginPage(driver)
    pim_page = PIMPage(driver)

    # 1. Abrir página de login
    login_page.open()

    # 2. Fazer login com usuário e senha válidos
    login_page.fill_username("Admin")
    login_page.fill_password("admin123")
    login_page.submit()
    assert login_page.is_dashboard_displayed(), "Falha no login"

    # 3. Navegar até módulo PIM
    pim_page.navigate_to_pim()

    # 4. Clicar no botão para adicionar novo empregado
    pim_page.click_add_employee()

    # 5. Preencher e salvar empregado
    first_name = "John"
    last_name = "Doe"
    pim_page.add_employee(first_name, last_name)

    # 6. Validar dados do perfil automaticamente exibido
    profile_first_name = pim_page.get_profile_first_name()
    profile_last_name = pim_page.get_profile_last_name()

    assert profile_first_name == first_name, f"Esperado first name '{first_name}', mas foi '{profile_first_name}'"
    assert profile_last_name == last_name, f"Esperado last name '{last_name}', mas foi '{profile_last_name}'"
