# twitterbot.main - Automatiza interações no Twitter.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

class Bot:
    def __init__(self, login, pswd):
        self.login = login
        self.pswd = pswd

    def entrar(self):
        driver = webdriver.Firefox()
        driver.get("https://twitter.com/login?lang=pt")
        time.sleep(random.randint(1,3))
        elem_login = driver.find_element_by_xpath("//input[@name='text'][@type='text']")
        elem_login.click()
        time.sleep(random.randint(0,2))
        elem_login.clear()
        elem_login.click()
        time.sleep(random.randint(1,2))
        elem_login.send_keys(self.login)

    def comentar(self, comentario):
        self.comentario = comentario
        pass

    def curtir():
        pass

    def sair(self):
        driver.close()

if __name__=='__main__':
    bot = Bot('login','senha')
    bot.entrar()
    bot.sair()

