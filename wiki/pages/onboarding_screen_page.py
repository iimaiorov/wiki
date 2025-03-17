import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class OnboardingScreenPage:
    def __init__(self):
        self.skip_button = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')
        self.forward_button = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        self.primary_text = (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        self.final_button = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')

    def skip_onboarding(self):
        with allure.step('Skip welcome screen'):
            browser.element(self.skip_button).click()

    def click_forward_button(self):
        with allure.step('Click on the forward button'):
            browser.element(self.forward_button).click()

    def click_done_button(self):
        with allure.step('Click on the final button'):
            browser.element(self.final_button).click()

    def should_have_first_window(self):
        with allure.step('Check welcome screen'):
            browser.element(self.primary_text).should(have.text('The Free Encyclopedia'))

    def should_have_new_way_window(self):
        with allure.step('Check the text on the "New ways to explore" screen'):
            browser.element(self.primary_text).should(have.text('New ways to explore'))

    def should_have_reading_lists_window(self):
        with allure.step('Check the text on the "Reading lists with sync" screen'):
            browser.element(self.primary_text).should(have.text('Reading lists with sync'))

    def should_have_data_and_privacy_window(self):
        with allure.step('Check the text on the "Data & Privacy" screen'):
            browser.element(self.primary_text).should(have.text('Data & Privacy'))


onboarding_screen_page = OnboardingScreenPage()
