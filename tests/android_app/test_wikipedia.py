import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure import step


def test_search():
    with step('Skip welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search request'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Поиск по Википедии')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Python')

    with step('Check search results'):
        result = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        result.should(have.size_greater_than(0))
        result.first.should(have.text('Python'))

def test_reading_list_tab():
    with step('Skip welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Open saved articles'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Сохранённые')).click()

    with step ('Close sychronization notification'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/negativeButton')).click()

    with step('Check saved articles'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/empty_title')).should(have.text('Ещё нет списков для чтения'))