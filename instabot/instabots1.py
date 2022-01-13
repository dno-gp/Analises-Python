# instabot.py - Realiza automação de interações no Instagram.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

class Bots1():
    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd
        
        self.driver = webdriver.Firefox()

    def acessar(self):      
        driver = self.driver
        driver.get("https://www.instagram.com/?hl=pt-br")
        time.sleep(1)
        
        elem_user = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]\
                                                  /div[1]/div/form/div[2]/div/label/input").send_keys(f"{self.login}") #TODO Observar o pep8
        time.sleep(2)
        elem_passwd = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]\
                                                    /div[1]/div/form/div[3]/div/label/input") #TODO Observar o pep8
                                                   
        elem_passwd.send_keys(f"{self.passwd}")
        time.sleep(1)
        elem_passwd.send_keys(Keys.RETURN)
        time.sleep(4)

        '''
        Após a inserção de dados do usuário, 
        é necessário um tempo de espera para
        que a sessão do usuário seja totalmente
        carregada.
        '''
    
    def curtir(self, hashtag):
        self.hashtag = hashtag
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+ self.hashtag +'/?hl=pt-br')
        time.sleep(2)

        for i in range(1, 15):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        hrefs = driver.find_elements_by_tag_name('a')

        pics = [elem.get_attribute('href') for elem in hrefs]

        for pic in pics[8:-15]:
            driver.get(pic)


            try: 
                elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/div/div/div[2]") #TODO Observar o pep8                                   
                time.sleep(1)
                actionchains = ActionChains(driver)
                actionchains.double_click(elem).perform()
                time.sleep(4)   

            except Exception as e:
                print("Erro: Curtida não efetuada.")
                time.sleep(4)
                
    def comentar(self, coment):
        self.coment = coment
        driver = self.driver
        driver.get('https://www.instagram.com/p/CYi_XKbLTvX/')
        time.sleep(2)
        elem_coment = driver.find_element_by_class_name('Ypffh')
        print("Elemento encontrado")
        time.sleep(1)
        elem_coment.click()
        time.sleep(random.randint(1,2))
        elem_coment = driver.find_element_by_class_name('Ypffh')
        elem_coment.clear()
        for letra in self.coment:
            elem_coment.send_keys(letra)
            time.sleep(random.randint(0,1))

        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/\
                                     div[1]/article/div/div[2]/div/div[2]/\
                                     section[3]/div/form/button[2]").click()
        #elem_coment.send_keys(Keys.RETURN)

    def finalizar(self):
        driver = self.driver
        driver.close()

        


if __name__ == '__main__':

    bot = Bots1("", "*")

    bot.acessar()

    try:
        for i in [""]: #Lista de hashtags
            bot.curtir(i)
    except:
        print("Erro")
    finally: 
        bot.finalizar()
