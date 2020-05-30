from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_PO.page.base_page import BasePage


class Contact(BasePage):
    def get_members(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')))
        members = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        list1 = []
        while True:
            contactlist:str = self.driver.find_element(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            print(contactlist)
            currnt,all = [int(i) for i in contactlist.split('/',1)]
            if currnt <= all:
                for member in members:
                    list1.append(member.get_attribute('title'))
                # currnt = currnt + 1
            print(list1)
            return list1

    def set_department(self):
        #点击全选按钮
        WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,'th.member_colRight_memberTable_th_Checkbox')))
        self.driver.find_element(By.CSS_SELECTOR,'th.member_colRight_memberTable_th_Checkbox').click()
        #点击设置所在部门按钮
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'a.qui_btn.ww_btn.js_move')))
        # sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,'a.qui_btn.ww_btn.js_move').click()
        #添加到舞蹈部
        # sleep(10)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))]//*[@id="1688850247513857_anchor"]')))
        self.driver.find_element(By.XPATH,'//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))]//*[@id="1688850247513857_anchor"]').click()
        #点击确认添加到该部门
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))] //*[@class="qui_btn ww_btn ww_btn_Blue js_submit"]')))
        self.driver.find_element(By.XPATH,'//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))] //*[@class="qui_btn ww_btn ww_btn_Blue js_submit"]').click()

        #获取现有成员的部门信息
        self.driver.refresh() #刷新界面
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')))
        members = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(4)')
        list2 = []
        while True:
            contactlist:str = self.driver.find_element(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            print(contactlist)
            currnt,all = [int(i) for i in contactlist.split('/',1)]
            if currnt <= all:
                for member in members:
                    list2.append(member.get_attribute('title'))
            print(list2)
        return list1
