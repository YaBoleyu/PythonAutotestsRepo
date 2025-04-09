import allure
import tests.pages.BigPage
import test_base
import utils.variables
from playwright.sync_api import expect

from tests.pages import BigPage

@allure.feature("Example tests")
class TestExample:
    @allure.story("Check page title")
    def test_example_page(self, page):
        with allure.step("Open" + test_base.AutomationPageUrl):
            page.goto(test_base.AutomationPageUrl)

        with allure.step("Check title"):
            expect(page).to_have_title("Automation Practice - Ultimate QA")

        with allure.step("Take screenshot"):
            page.screenshot(path=test_base.ScreenshotsPath+"example.png")
            allure.attach.file(test_base.ScreenshotsPath+"example.png", name="screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.story("Open Big page with many elements")
    def test_open_services(self,page):
        with allure.step("Open Big page url"):
            page.goto(test_base.BigPageUrl)
        with allure.step("Check title"):
            expect(page).to_have_title("Complicated Page - Ultimate QA")
        with allure.step("Take screenshot"):
            page.screenshot(path=test_base.ScreenshotsPath+"example.png")
            allure.attach.file(test_base.ScreenshotsPath+"example.png", name="screenshot", attachment_type=allure.attachment_type.PNG)

