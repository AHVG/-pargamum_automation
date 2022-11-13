
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException

from datetime import date

from element_finder import ElementFinder
from exceptions import ElementNotFoundException, NoBooksException

class NoFine:

    def __init__(self, password='', login='', browser=None):
        self.__login = login
        self.__password = password
        self.__browser = browser

    def get_login(self):
        return self.__login

    def set_login(self, new_login):
        self.__login = new_login

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_browser(self):
        return self.__browser

    def set_browser(self, new_browser):
        self.__browser = new_browser
    
    def enter_pergamun(self):

        path_login = 'username'
        path_passwrod = 'password'
        path_button = '//*[@id="pergamum"]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/button[1]'

        login_field = ElementFinder().find_element(self.get_browser(), By.NAME, path_login)
        password_field = ElementFinder().find_element(self.get_browser(), By.NAME, path_passwrod)
        enter_button = ElementFinder().find_element(self.get_browser(), By.XPATH, path_button)

        login_field.clear()
        password_field.clear()
        login_field.send_keys(self.get_login())
        password_field.send_keys(self.get_password())
        enter_button.click()

    def exit_pergamun(self):
        path_button = '/html/body/div[8]/a/img'
        logout_button = ElementFinder().find_element(self.get_browser(), By.XPATH, path_button)

        logout_button.click()

    def exit_webdriver(self):
        path_body = '/html/body'
        ElementFinder().find_element(self.get_browser(), By.XPATH, path_body)

        self.get_browser().close()
        self.get_browser().quit()

    def renew_books(self):
        path_buttons = 'btn_renovar'

        try:
            renew_buttons = ElementFinder().find_elements(self.get_browser(), By.CLASS_NAME, path_buttons)
        except ElementNotFoundException as e:
            raise NoBooksException()

        for index in range(len(renew_buttons)):
            path_title = f'/html/body/div[13]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td/div/div[1]/div[2]/table/tbody/tr[{index + 2}]/td[2]/a'
            title = ElementFinder().find_element(self.get_browser(), By.XPATH, path_title)
            title = title.text.strip().replace(" - Livros", "")

            path_date = f'/html/body/div[13]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td/div/div[1]/div[2]/table/tbody/tr[{index + 2}]/td[3]'
            delivery_date = ElementFinder().find_element(self.get_browser(), By.XPATH, path_date)
            delivery_date = [int(x) for x in delivery_date.text.strip().split("/")]

            today_date = date.today()
            today_date = [today_date.day, today_date.month, today_date.year]

            if today_date == delivery_date:
                renew_buttons[index].click()
                path_back_button = 'btn_voltar'
                back_button = ElementFinder().find_element(self.get_browser(), By.CLASS_NAME, path_back_button)
                back_button.click()

            renew_buttons = ElementFinder().find_elements(self.get_browser(), By.CLASS_NAME, path_buttons)

    def run(self):
        try:
            self.enter_pergamun()
            self.renew_books()
            self.exit_pergamun()
        except ElementNotFoundException as e:
            print(e)
        except NoBooksException as e:
            print(e)
        except NoSuchWindowException as e:
            print("Interrupted renewal process!")
        else:
            self.exit_webdriver()

