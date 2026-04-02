# AI-Powered Self-Healing Test Automation Framework

Production-grade QA automation framework with self-healing locators, AI-generated test cases, and automated failure analysis.

---

## 🚀 Problem Statement

Traditional automation frameworks suffer from:

- Brittle locators causing flaky tests
- High debugging time due to poor failure visibility
- Manual effort in writing and maintaining test cases

This framework addresses these challenges using AI-driven capabilities to improve reliability, speed, and intelligence in test automation.

---

## 🧠 Key Features

- **Self-Healing Locator Engine**
  - Multi-fallback locator strategy (CSS, XPath, text)
  - Automatic recovery from locator failures
  - Heal events logged for analysis

- **AI Test Case Generator**
  - Generates structured test cases using LLM
  - Stores output in JSON format
  - Enables scalable test design

- **AI Failure Analyzer**
  - Captures screenshot and logs on failure
  - Generates root cause analysis using AI
  - Outputs structured `failure_report.json`

- **Allure Reporting Integration**
  - Step-level execution visibility
  - Screenshots attached to every test
  - AI insights attached on failures
  - Heal logs included in report

- **CI/CD Pipeline (GitHub Actions)**
  - Runs on every push
  - Executes full test suite
  - Uploads Allure results as artifacts

---

## 🏗️ Architecture
Tests → Page Objects → BasePage → Smart Locator Engine
↓
Heal Logs

Failures → Screenshot + Logs → AI Analyzer → failure_report.json

Execution → Pytest → Allure Reports

CI/CD → GitHub Actions → Allure Artifacts


## 🎯 Demo Scenarios

### 1. Successful Login Flow
- Executes end-to-end login test
- Visible step-level reporting in Allure

### 2. Failure Analysis
- Intentional test failure
- AI generates root cause analysis automatically
- Output available in Allure report

### 3. Self-Healing Execution
- Primary locator intentionally broken
- Fallback locator used successfully
- Heal event logged in `heal_log.json`

---

## ⚙️ Tech Stack

- Python
- Pytest
- Selenium WebDriver
- WebDriver Manager
- Allure Reporting
- OpenAI API (LLM integration)
- GitHub Actions (CI/CD)

---

## 📦 Project Structure
ai-powered-qa-framework
│
├── base/ # BasePage with reusable actions
├── pages/ # Page Object Models
├── tests/ # Test cases
├── utils/ # Smart locator + logs
├── ai_modules/ # AI integrations
├── reports/ # Allure results & failure artifacts
├── conftest.py # Pytest fixtures and hooks
└── .github/workflows/ # CI pipeline
---

## ▶️ How to Run

``bash
pip install -r requirements.txt
pytest --alluredir=reports/allure-results
allure serve reports/allure-results


📎 Author
Rupender Singh
QA Engineering Leader | AI-Powered Test Automation | BFSI Domain
