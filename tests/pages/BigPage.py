from playwright.sync_api import Page


class BigPage:
    def __init__(self, page: Page):
        self.page = Page

    skillsImprovedTitle = "//span[@id = 'Skills_Improved']"
    sectionOfButtons = "//span[@id = 'Section_of_Buttons']"
    buttons = "//div/a[contains(@class, 'et_pb_button et_pb_button')]"
    sectionOfSocialMediaFollows = "//span[@id = 'Section_of_Social_Media_Follows']"
    twitterButton = "(//li/a[@title ='Follow on Twitter'])[1]"
    facebookButton = "(//li/a[@title ='Follow on Facebook'])[1]"
    sectionOfRandomStuff = "//span[@id = 'Section_of_Random_Stuff']"
