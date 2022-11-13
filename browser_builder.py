
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import InvalidArgumentException


class BrowserBuilder:

    def create(self, url):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        browser = webdriver.Chrome(service = service, options=options)
        try:
            browser.get(url)
            return browser
        except InvalidArgumentException as e:
            print("Error InvalidArgumentException")
            return None
