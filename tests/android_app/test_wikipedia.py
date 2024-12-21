from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Python')
    result = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    result.should(have.size_greater_than(0))
    result.first.should(have.text('Python'))

