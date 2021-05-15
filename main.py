from selenium import webdriver
from time import sleep
import os

class InstaBot:
    def __init__ (self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
            sleep(4)
            self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except:
            print('The Save password or Notifications enable popup did not occur did not occur')
        sleep(2)
        self.driver.find_element_by_xpath('//a[contains(text(), "aditya_1729sg")]').click()


    def get_followings(self):
        sleep(2)
        self.driver.find_element_by_xpath('//a[contains(@href, "/following")]').click()
        sleep(1)
        try:
            sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggessions)]')
            self.driver.execute_script('arguements[0].scrollIntoView()', sugs)
            sleep(1)
        except:
            print('No suggessions')
            pass
        print('Scroll to the bottom')
        sleep(2) 
        

    def get_followers(self):
        self.driver.find_element_by_xpath('//a[contains(@href, "/followers")]').click()
        sleep(1)
        try:
            sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggessions)]')
            self.driver.execute_script('arguements[0].scrollIntoView()', sugs)
            sleep(1)
        except:
            print('No suggessions')
            pass
        print('Scroll to the bottom')
        sleep(2)

    def _get_names(self):
        links = self.driver.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        listone = names
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button/div').click()
        return listone



# mybot = InstaBot('aditya26sg@gmail.com', 'Shivbaba26$')


# To run an interactive shell use the command 'python3 -i main.py' then you can 
# type 'mybot.get_unfollowers()' anytime in the program and till then the selenium
# will wait