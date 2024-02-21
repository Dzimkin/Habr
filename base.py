from typing import Callable
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://habr.com')

    def find(self, presence: Callable, timeout: int) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(presence)

    def find_element(self, locator: tuple[str, str], timeout=10) -> WebElement:
        return self.find(EC.presence_of_element_located(locator), timeout)

    def find_elements(self, locator: tuple[str, str], timeout=10) -> list[WebElement]:
        return self.find(EC.presence_of_all_elements_located(locator), timeout)

    def press_enter(self, element: WebElement):
        element.send_keys(Keys.RETURN)
