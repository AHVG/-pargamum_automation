
import argparse
import sys
from credential_builder import CredentialBuilder
from browser_builder import BrowserBuilder
from no_fine import NoFine


class App:

    def __init__(self):
        parser = argparse.ArgumentParser(add_help=False)
        parser.version = '1.0'
        parser.add_argument('-h', '--help', action='help', help='Program to automate book renewal')
        parser.add_argument('-v', '--version', action='version')

        self.__parser = parser
        self.__credential_builder = CredentialBuilder()
        self.__browser_builder = BrowserBuilder()
        self.__bot = NoFine()

    def run(self):
        browser = self.__browser_builder.create("https://pergamum.ufsc.br/login?redirect=/meupergamum")
        login, password = self.__credential_builder.create(self.__parser)

        if browser is None:
            sys.exit()

        self.__bot.set_browser(browser)
        self.__bot.set_login(login)
        self.__bot.set_password(password)
        self.__bot.run()

