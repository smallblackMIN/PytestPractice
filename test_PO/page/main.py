from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_PO.page.add_member_page import AddMember
from test_PO.page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

from test_PO.page.contact_page import Contact


class Main(BasePage):
    def goto_add_member(self):
        #点击添加成员
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)')))
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self.driver)
    def goto_edit_contact(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable)
        #编辑通讯录
        self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()
        return Contact(self.driver)