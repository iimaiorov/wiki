import allure
from wiki.pages.main_page import main_page
from wiki.pages.onboarding_screen_page import onboarding_screen_page



@allure.epic('Главная страница')
@allure.story('Поиск статей')
class TestSearch:
    def test_search(self):
        title = 'Python'

        onboarding_screen_page.skip_onboarding()

        main_page.should_have_main_page()
        main_page.search(title)

        main_page.should_have_search_results(title)


