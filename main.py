import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from datetime import date


class BotFinesNeverAgain:


    def __init__(self):
        self.login = sys.argv[1]
        self.password = sys.argv[2]
        self.wait_time = 60
        self.browser = None

    def enter_pergamun(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(service = service, options=options)
        self.browser.get("https://pergamum.ufsc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php")

        login_field = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.NAME, 'login')))
        password_field = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        login_field.clear()
        password_field.clear()
        login_field.send_keys(self.login)
        password_field.send_keys(self.password)

        enter_button = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.NAME, 'button')))
        enter_button.click()

    def exit_pergamun(self):
        logout_button = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/a/img')))
        logout_button.click()

    def exit_webdriver(self):

        WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.XPATH, '/html/body')))
        self.browser.close()
        self.browser.quit()

    def renew_books(self):
        renew_buttons = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn_renovar')))
        for index in range(len(renew_buttons)):
            title = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[13]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td/div/div[1]/div[2]/table/tbody/tr[{index + 2}]/td[2]/a')))
            title = title.text.strip().replace(" - Livros", "")

            delivery_date = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[13]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td/div/div[1]/div[2]/table/tbody/tr[{index + 2}]/td[3]')))
            delivery_date = [int(x) for x in delivery_date.text.strip().split("/")]

            today_date = date.today()
            today_date = [today_date.day, today_date.month, today_date.year]

            if today_date == delivery_date:
                renew_buttons[index].click()
                back_button = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_voltar')))
                back_button.click()

            renew_buttons = WebDriverWait(self.browser, self.wait_time).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn_renovar')))

    def run(self):
        try:
            self.enter_pergamun()
            self.renew_books()
            self.exit_pergamun()
        except TimeoutException as e:
            print("Error: TimeoutException")
            print("HTML component not found!")
        self.exit_webdriver()


bot = BotFinesNeverAgain()
bot.run()
