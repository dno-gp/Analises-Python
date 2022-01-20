# twitterbot/main.py - Automatiza interações no Twitter.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
import os

class Bot:
    def __init__(self, login, pswd):
        self.login = login
        self.pswd = pswd
        self.driver = webdriver.Firefox()

    def entrar(self):
        self.driver.get("https://twitter.com/login?lang=pt")
        time.sleep(5)

        #Login
        elem_login = self.driver.find_element(
                                        By.XPATH,
                                        "//input[@name='text'][@type='text']"
                                        )
        elem_login.click()
        time.sleep(2)
        elem_login.clear()
        elem_login.click()
        time.sleep(random.randint(1,2))
        elem_login.send_keys(self.login)
        elem_login.send_keys(Keys.RETURN)
        time.sleep(random.randint(3,4))

        #Password
        elem_psw = self.driver.find_element(
                                      By.XPATH,
                                 "//input[@name='password'][@type='password']"
                                      )
        elem_psw.click()
        time.sleep(random.randint(1,2))
        elem_psw.clear()
        elem_psw.click()
        time.sleep(random.randint(1,3))
        for char in self.pswd:
            elem_psw.send_keys(char)
            time.sleep(random.randint(0,1))

        elem_psw.send_keys(Keys.RETURN)

    def twitter(self, tw):
        self.tw = tw
        self.driver.get("https://twitter.com/compose/tweet")
        time.sleep(random.randint(2,3))
        elem_box = self.driver.find_element(By.XPATH,
                                           "//div[@role='textbox']")
        time.sleep(random.randint(1,2))
        for char in self.tw:
            elem_box.send_keys(char)
            time.sleep(random.randint(0,1))

        elem_bt = self.driver.find_element(By.XPATH,
                                          "//div[@role='button'][@data-testid='tweetButton']")
        time.sleep(random.randint(1,2))
        elem_bt.click()

    def comentar(self, comentario):
        self.comentario = comentario
        pass

    def curtir():
        pass

    def sair(self):
        driver = webdriver.Firefox()
        driver.close()

if __name__=='__main__':
    bot = Bot(os.environ.get('LOGIN_TW'), os.environ.get('PSW_TW'))
    bot.entrar()
    bot.twitter("Boa tarde!")
