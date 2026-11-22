# UI-тесты Stellar Burgers

Автотесты для образовательного веб-приложения Stellar Burgers. Проект использует Selenium, Pytest, паттерн Page Object Model и Allure-отчёт. Тесты запускаются в Google Chrome и Mozilla Firefox.

## Требования

- macOS или другая поддерживаемая операционная система
- Python 3.10 или новее
- Google Chrome
- Mozilla Firefox
- Allure Commandline для формирования HTML-отчёта

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

В VS Code выберите интерпретатор `.venv/bin/python` через `Python: Select Interpreter`.

## Настройка аккаунта

По умолчанию фикстура создаёт временного пользователя через API и удаляет его после теста.

Для использования постоянного аккаунта создайте `.env` по образцу `.env.example`:

```dotenv
BASE_URL=https://qa-stellarburgers.education-services.ru
API_URL=https://qa-stellarburgers.education-services.ru/api
STELLAR_EMAIL=qa@example.com
STELLAR_PASSWORD=QaPassword123
```

## Запуск тестов

Запустить все тесты в Chrome и Firefox:

```bash
pytest
```

Запустить тесты только в одном браузере:

```bash
pytest -k chrome
pytest -k firefox
```

Запустить конкретный модуль:

```bash
pytest tests/test_account.py
```

Результаты Allure сохраняются в папку `results/`.

## Просмотр Allure-отчёта

```bash
allure serve results
```

Или сформировать статический отчёт:

```bash
allure generate results --clean -o allure-report
allure open allure-report
```

## Структура проекта

- `pages/` - Page Object классы;
- `locators/` - локаторы элементов;
- `tests/` - тестовые сценарии;
- `conftest.py` - фикстуры драйверов и тестового аккаунта;
- `pytest.ini` - настройки Pytest и Allure;
- `results/` - результаты Allure после запуска;
- `.env.example` - пример конфигурации.