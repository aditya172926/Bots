from selenium import webdriver
from time import sleep

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


mybot = InstaBot('aditya26sg@gmail.com', 'Shivbaba26$')