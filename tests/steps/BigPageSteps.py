import time

import allure
from playwright.async_api import expect

from tests.pages import BigPage
from tests.tests.MainTests import test_base


def clickOnButtons(page):
    i = 0
    buttons = page.locator(BigPage.BigPage.buttons).all()
    for button in buttons:
        button.click()
        i += 1
        page.screenshot(path=test_base.ScreenshotsPath + "ButtonClicked" + str(i) + ".png")


def validateSocialMedia(page):
    twitter = "x.com"
    facebook = "facebook.com"
    with allure.step("Twitter"):
        page.locator(BigPage.BigPage.twitterButton).click()
    with allure.step("URL после перехода"):
        page.wait_for_url()
        current_url = page.url
        print(f"Current URL: {current_url}")
        allure.attach(f"Redirected to: {current_url}", name="Redirect info")
        assert current_url.contains(twitter)
    with allure.step("Facebook"):
        page.locator(BigPage.BigPage.facebookButton).click()
    with allure.step("URL после перехода"):
        time.sleep(2)
        current_url = page.url
        print(f"Current URL: {current_url}")
        allure.attach(f"Redirected to: {current_url}", name="Redirect info")
        assert facebook in current_url
