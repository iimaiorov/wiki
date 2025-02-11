import pytest
import allure_commons
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support

import project
from utils import allure


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = project.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0
    browser.config._wait_decorator = support._logging.wait_with(
        context = allure_commons._allure.StepContext
    )

    yield

    allure.attach_screenshot()
    allure.attach_page_source()
    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        allure.attach_bstack_video(session_id)