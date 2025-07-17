import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_settings():
    browser.config.driver_name = "firefox"
    browser.config.window_height = 768
    browser.config.window_width = 1024