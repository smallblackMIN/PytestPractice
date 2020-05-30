from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self,driver1=None):
        if driver1 == None:
            option = Options()
            option.debugger_address = 'localhost:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            # self.driver.implicitly_wait(15)
            #WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable)
        else:
            self.driver = driver1



