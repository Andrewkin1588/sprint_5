import time

from selenium.webdriver.common.by import By
from locators import Constructor
from src import constants

class TestChapter:

    def test_chapter(self, driver, helpers):
        driver.get(constants.BASE_URL)  # Переходим на главную

        tab_text = driver.find_elements(By.XPATH, Constructor.CONSTRUCTOR_TAB_TEXT)
        tabs_select = driver.find_elements(By.XPATH, Constructor.CONSTRUCTOR_TAB)
        name_chapter = ['Булки', 'Соусы', 'Начинки']

        for tab in range(len(tabs_select)):
            assert tab_text[tab].text == name_chapter[tab]
            driver.execute_script("arguments[0].click();", tabs_select[tab])