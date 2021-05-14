from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

class InstaBot:
    def __init__ (self):
        driver.get('https://www.instagram.com/')
        sleep(2)
        

InstaBot()