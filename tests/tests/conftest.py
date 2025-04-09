import pytest
from playwright.sync_api import Playwright, APIRequestContext, sync_playwright


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

import asyncio
import pytest

@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.WindowsProactorEventLoopPolicy()  # Для Windows
    loop = policy.new_event_loop()
    yield loop
    if not loop.is_running():
        loop.close()