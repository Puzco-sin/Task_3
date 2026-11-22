import os
import uuid

import allure
import pytest
import requests
from dotenv import load_dotenv
from selenium import webdriver


load_dotenv()


BASE_URL = os.getenv("BASE_URL", "https://qa-stellarburgers.education-services.ru")
API_URL = os.getenv("API_URL", f"{BASE_URL}/api")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def account():
    email = os.getenv("STELLAR_EMAIL")
    password = os.getenv("STELLAR_PASSWORD")

    if email and password:
        return email, password

    unique = uuid.uuid4().hex
    email = f"qa_{unique}@example.com"
    password = "QaPassword123"
    response = requests.post(
        f"{API_URL}/auth/register",
        json={"email": email, "password": password, "name": "QA User"},
        timeout=15,
    )
    response.raise_for_status()
    token = response.json()["accessToken"]

    yield email, password

    requests.delete(
        f"{API_URL}/auth/user",
        headers={"Authorization": token},
        timeout=15,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
