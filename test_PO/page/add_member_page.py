from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_PO.page.base_page import BasePage
from test_PO.page.contact_page import Contact


class AddMember(BasePage):

    def add_member(self):
        #输入姓名
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'username')))
        self.driver.find_element(By.ID,'username').send_keys('七岁')
        #账号
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'memberAdd_acctid')))
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('26')
        #手机号
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'memberAdd_phone')))
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys('15209870167')
        #点击保存
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.js_btn_save')))
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        return Contact(self.driver)