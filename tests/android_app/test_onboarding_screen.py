import allure
from wiki.pages.onboarding_screen_page import onboarding_screen_page
from wiki.pages.main_page import main_page


@allure.epic('Onboarding screen')
@allure.story('Verification of the welcome screen')
class TestOnboardingScreen:
    @allure.title('Verification of the welcome screen')
    def test_get_started(self):
        onboarding_screen_page.should_have_first_window()
        onboarding_screen_page.click_forward_button()

        onboarding_screen_page.should_have_new_way_window()
        onboarding_screen_page.click_forward_button()

        onboarding_screen_page.should_have_reading_lists_window()
        onboarding_screen_page.click_forward_button()

        onboarding_screen_page.should_have_data_and_privacy_window()
        onboarding_screen_page.click_done_button()

        main_page.should_have_main_page()
