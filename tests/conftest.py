import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({  # опции для запуска теста на android, именно локальные опции
        # Specify device and os_version for testing
        "platformName": "android",
        # Название платформы, это не обязательно указывать, так как по умолчанию стоит android
        "platformVersion": "9.0",  # Версия Android
        "deviceName": "Google Pixel 3",  # Имя устройства в Browserstack

        # Set URL of the application under test
        "app": "bs://sample.app",
        # Ссылка на загруженное приложение в Browserstack. Если стандартное приложение, то оставить как есть

        # Set other BrowserStack capabilities (опции именно для Browserstack)
        'bstack:options': {
            "projectName": "First Python project",  # Название проекта которое будет отображаться в Browserstack
            "buildName": "browserstack-build-1",  # Название сборки которое будет отображаться в Browserstack
            "sessionName": "BStack first_test",  # Название сессии которое будет отображаться в Browserstack

            # Set your access credentials
            "userName": "yuramayorov_r0RgK5",  # Ваш логин в Browserstack
            "accessKey": "TpJicZDk8Y2oTAYSw3uQ"  # Ваш ключ доступа в Browserstack
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub",
                                             options=options)  # Адрес для подключения к Browserstack

    browser.config.timeout = float(os.getenv('timeout', '10.0'))  # Таймаут для ожидания элементов

    # тут можно добавить низкоуровневое логирование шагов

    session_id = browser.driver.session_id  # Получаем ID сессии

    yield

    # аттачи
    browser.quit()