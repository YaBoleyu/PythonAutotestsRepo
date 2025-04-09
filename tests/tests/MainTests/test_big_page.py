import allure
import test_base
import pytest
from tests.steps import BigPageSteps
from playwright.async_api import Page

@allure.testcase("Click on Buttons Test")
async def test_click_on_buttons(page):
    with allure.step("Open Big page url"):
        await page.goto(test_base.BigPageUrl)
    with allure.step("Click on buttons"):
        await BigPageSteps.clickOnButtons(page)


@allure.testcase("Social Media Test")
def test_validate_social_media(page: Page):
    page.goto(test_base.BigPageUrl)
    BigPageSteps.validateSocialMedia(page)
