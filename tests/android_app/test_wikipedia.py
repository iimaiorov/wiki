import allure
from wiki.pages.main_page import main_page
from wiki.pages.onboarding_screen_page import onboarding_screen_page


@allure.epic('Main page')
@allure.story('Search')
class TestSearch:
    @allure.title('Search')
    def test_search(self):
        title = 'Python'

        onboarding_screen_page.skip_onboarding()

        main_page.should_have_main_page()
        main_page.search(title)

        main_page.should_have_search_results(title)

    @allure.title('Open search result')
    def test_open_search_result(self):
        title = 'Python'

        onboarding_screen_page.skip_onboarding()

        main_page.should_have_main_page()
        main_page.search(title)

        main_page.should_have_search_results(title)

        main_page.open_search_result(title)
        main_page.should_have_article(title)
