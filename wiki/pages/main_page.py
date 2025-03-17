import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.search_field = (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
        self.search_input = (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
        self.search_results = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        self.main_page_title = (AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')

    def should_have_main_page(self):
        with allure.step('Check main page'):
            browser.element(self.main_page_title).should(have.text('Customize your Explore feed'))

    def search(self, text: str):
        with allure.step(f'Type search request: {text}'):
            browser.element(self.search_field).click()
            browser.element(self.search_input).type(text)

    def should_have_search_results(self, text: str):
        with allure.step('Check search results'):
            result = browser.all(self.search_results).should(have.size_greater_than(0))
            result.should(have.size_greater_than(0))
            result.first.should(have.text(text))

    def open_search_result(self, text: str):
        with allure.step(f'Open search result: {text}'):
            browser.element(self.search_results).click()

    def should_have_article(self, text: str):
        with allure.step('Check article'):
            browser.element((AppiumBy.XPATH, f'//android.webkit.WebView[@text="{text}"]')).should(have.text(text))


main_page = MainPage()
