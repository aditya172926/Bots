from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

class LinkedinBot:
    def __init__(self, email, password):
        self.email = email
        driver.get('https://www.linkedin.com/')
        sleep(2)
        driver.find_element_by_xpath("//input[@name=\"session_key\"]").send_keys(email)
        driver.find_element_by_xpath("//input[@name=\"session_password\"]").send_keys(password)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        done = input('If 2 factor authentication enabled, please continue your login and type "y" for yes, "n" for no')
        if done == 'y':
            sleep(3)
            driver.find_element_by_xpath("//a[@data-control-name=\"nav_mynetwork\"]").click()
        else:
            pass

LinkedinBot('aditya26sg@gmail.com', 'Chocolate26$')
