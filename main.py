from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
driver.maximize_window()

class InstaBot:
    def __init__ (self, username, pw):
        self.username = username

        driver.get('https://www.instagram.com/')
        sleep(2)
        driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
            sleep(4)
            driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except:
            print('The Save password or Notifications enable popup did not occur did not occur')

    def get_unfollowers(self):
        driver.find_element_by_xpath('//a[contains(text(), "aditya_1729sg")]').click()
        sleep(4)
        driver.find_element_by_xpath('//a[contains(@href, "/following")]').click()
        sleep(1)
        try:
            sugs = driver.find_element_by_xpath('//h4[contains(text(), Suggessions)]')
            driver.execute_script('arguements[0].scrollIntoView()', sugs)
            sleep(1)
        except:
            print('No suggessions')
            pass
        print('Scroll to the bottom')
        sleep(2) 
        done = input("Are you done?")
        following = self._get_names()

        driver.find_element_by_xpath('//a[contains(@href, "/followers")]').click()
        sleep(1)
        try:
            sugs = driver.find_element_by_xpath('//h4[contains(text(), Suggessions)]')
            driver.execute_script('arguements[0].scrollIntoView()', sugs)
            sleep(1)
        except:
            print('No suggessions')
            pass
        print('Scroll to the bottom')
        sleep(2) 
        done = input("Are you done?")
        followers = self._get_names()

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        links = driver.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button/div').click()
        return names



mybot = InstaBot('aditya26sg@gmail.com', 'Shivbaba26$')


# To run an interactive shell use the command 'python3 -i main.py' then you can 
# type 'mybot.get_unfollowers()' anytime in the program and till then the selenium
# will wait