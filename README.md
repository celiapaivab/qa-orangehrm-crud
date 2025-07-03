# Automação CRUD OrangeHRM

![QA](https://img.shields.io/badge/Testes-Automação-blue)
![Ferramenta](https://img.shields.io/badge/Selenium-Python-green)
![Tipo de Teste](https://img.shields.io/badge/Testes-Funcional-lightgrey)
![Python application](https://github.com/celiapaivab/qa-orangehrm-crud-
![Status](https://github.com/celiapaivab/qa-orangehrm-crud-internet/actions/workflows/python-app.yml/badge.svg?branch=main)

---

## 📌 Sobre o Projeto

Este projeto automatiza testes de operações CRUD (Create, Read, Update, Delete) de funcionários no sistema [OrangeHRM](https://opensource-demo.orangehrmlive.com/), uma solução open-source de gestão de recursos humanos.

---

## 🎯 Objetivo do Projeto
 
Garantir que as principais funcionalidades do módulo PIM do OrangeHRM funcionem corretamente por meio de testes automatizados, validando a qualidade da aplicação de forma contínua.

---

## 🔧 Tecnologias e Ferramentas

- Python
- Pytest
- Selenium WebDriver
- GitHub Actions

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/celiapaivab/qa-orangehrm-crud.git
cd qa-orangehrm-crud
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute os testes:

```bash
pytest tests/
```

---

## 🧾 Resultado

- Testes de login com credenciais válidas executados com sucesso.  
- Cadastro de novo funcionário realizado e validado.  
- Pesquisa, edição e exclusão de funcionário validadas com sucesso.  
- Validação de mensagens e comportamentos corretos após cada operação CRUD.  
- Estrutura modular com Page Object Model aplicada.  
- Pipeline configurado no **GitHub Actions** para executar os testes automaticamente a cada *push*.

---

## 📚 Aprendizados

- Implementação prática de testes automatizados com **Selenium** e **Pytest**.  
- Estruturação de testes para diferentes fluxos de CRUD de funcionários.  
- Integração dos testes automatizados em um pipeline **CI/CD** no **GitHub Actions**.  
- Boas práticas de organização e reutilização de código com o padrão **Page Object Model**.

---

## 💡 Melhorias Futuras

- Adicionar testes para fluxos negativos (ex.: login inválido, edição com dados em branco).  
- Implementar testes em múltiplos navegadores (**cross-browser**).  
- Criar relatórios de testes detalhados em HTML.  
- Integrar com ferramentas de rastreamento de bugs e geração automática de evidências.

---

## 📂 Arquivos do Projeto

- `tests/` – Scripts de teste automatizados para login, cadastro, edição e exclusão de funcionário  
- `pages/` – Page Object Model para as páginas do módulo PIM  
- `requirements.txt` – Dependências do projeto  
- `.github/workflows/` – Configuração do pipeline **GitHub Actions**

---

## 🇺🇸 Project Summary

This repository contains an automated test suite using **Selenium with Python** for the [OrangeHRM Open Source Demo](https://opensource-demo.orangehrmlive.com).  
The project validates the complete CRUD cycle for employees, with clear structure, maintainability, and real-world test automation practices.  
It follows the **Page Object Model**, uses **Pytest** for test execution and is designed to be easily extendable for new scenarios.
