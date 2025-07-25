# CRUD Test Automation — OrangeHRM

![QA](https://img.shields.io/badge/QA-Automation-blue)
![Tool](https://img.shields.io/badge/Selenium-Python-green)
![Test Type](https://img.shields.io/badge/Functional_Testing-lightgrey)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://github.com/celiapaivab/qa-orangehrm-crud)
[![Status](https://github.com/celiapaivab/qa-orangehrm-crud/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/celiapaivab/qa-orangehrm-crud/actions/workflows/python-app.yml)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0077B5?logo=linkedin)](https://www.linkedin.com/in/celia-bruno)

---

## 📌 Project Overview

This project automates functional tests for CRUD (Create, Read, Update, Delete) operations on employee records within the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) Open Source Demo, a free HR management system primarily used for training and demonstration purposes.

The tests are automated with the purpose of learning how to design and implement test automation using **Selenium**. Since the site is for demonstration only, no real bugs are expected or detected. This project serves solely as a training and study exercise.

---

## 🎯 Project Goal
 
- Validate that the core functionalities of the PIM (Personnel Information Management) module operate as intended.
- Implement automated functional tests to ensure reliability and correctness.
- Support continuous quality assurance through regular automated test execution.
- Specifically, automate tests for the following CRUD operations:
  - **Create:** Add new employee records successfully.
  - **Read:** Search and view employee details accurately.
  - **Update:** Edit and update employee information correctly.
  - **Delete:** Remove employee records and validate their deletion.

---

## 🔧 Technologies & Tools

- Python
- Pytest
- Selenium WebDriver
- GitHub Actions

---

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/celiapaivab/qa-orangehrm-crud.git
cd qa-orangehrm-crud
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the tests:

```bash
pytest tests/
```

---

## 🧾 Results

- Successful login tests with valid credentials executed.  
- New employee registration performed and validated.  
- Employee search, edit, and deletion successfully validated.  
- Validation of correct messages and behaviors after each CRUD operation.  
- Modular structure with Page Object Model applied.  
- Pipeline configured in **GitHub Actions** to run tests automatically on each *push*.

---

## 📚 What I Learned

- Practical implementation of automated tests with **Selenium** and **Pytest**.  
- Structuring tests for different employee CRUD flows.  
- Integration of automated tests into a **CI/CD** pipeline on **GitHub Actions**.  
- Best practices for code organization and reuse using the **Page Object Model** pattern.

---

## 💡 Future Improvements

- Add tests for negative flows (e.g., invalid login, editing with blank data).  
- Implement tests across multiple browsers (**cross-browser**).  
- Generate detailed HTML test reports.  
- Integrate with bug tracking tools and automatic evidence generation.

---

## 📂 Project Files

- `tests/` – Automated test scripts for employee login, creation, editing, and deletion  
- `pages/` – Page Object Model for the PIM module pages  
- `requirements.txt` – Project dependencies  
- `.github/workflows/` – Configuration of the **GitHub Actions** pipeline

---
