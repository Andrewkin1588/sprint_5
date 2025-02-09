from selenium import webdriver
from helpers import Helpers

import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def helpers():
    helper = Helpers()
    return helper
