
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from exceptions import ElementNotFoundException


class ElementFinder:

    def find_element(self, browser, by, path, wait_time=30):
        try:
            return WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((by, path)))
        except TimeoutException as e:
            raise ElementNotFoundException(by, path)

    def find_elements(self, browser, by, path, wait_time=30):
        try:
            return WebDriverWait(browser, wait_time).until(EC.presence_of_all_elements_located((by, path)))
        except TimeoutException as e:
            raise ElementNotFoundException(by, path)
