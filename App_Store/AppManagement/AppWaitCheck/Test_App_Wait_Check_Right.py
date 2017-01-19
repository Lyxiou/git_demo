# coding=utf-8

from selenium import webdriver
import unittest
from bsddb.test.test_all import suite
from lib2to3.tests.support import driver
from time import sleep
from selenium.webdriver.common.keys import Keys
from string import rstrip

class TestAppManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://10.110.1.55:8082/admin/home.html"
        #http://10.110.1.55:8082/login.html
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@value='登录']").click()
        sleep(1) 
        sreach_window = self.driver.current_window_handle    
        self.driver.find_element_by_link_text("应用管理").click()
        sleep(1)
        sreach_window = self.driver.current_window_handle 
        self.driver.find_element_by_link_text("待审核").click()
        sleep(1)        
    
    def check_drop_down_list_num_10(self):
        sreach_window = self.driver.current_window_handle
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys("j")
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
        
        #Refresh
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/button').click()
        sleep(1)
        #drop down list num items
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]').click()
        sleep(1)
        '''
        items = driver.find_elements_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/ul/li')
        for i in items:
            i.click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]').click()
            sleep(1)
        '''
        sleep(1)
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/ul/li[1]').click()
        numitemstext = driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/button/span[1]').text
        if (numitemstext == "10"):
            rst = True
        else:
            rst = False
        return rst
    def test_drop_down_list_num_10(self):
        result = self.check_drop_down_list_num_10()
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
        
    def check_drop_down_list_num_25(self):
        sreach_window = self.driver.current_window_handle
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys("j")
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
        
        #Refresh
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/button').click()
        sleep(1)
        #drop down list num items
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]').click()
        sleep(1)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/ul/li[2]').click()
        numitemstext = driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/button/span[1]').text
        if (numitemstext == "25"):
            rst = True
        else:
            rst = False
        return rst
    def test_drop_down_list_num_25(self):
        result = self.check_drop_down_list_num_25()
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
        
    def check_drop_down_list_num_50(self):
        sreach_window = self.driver.current_window_handle
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys("j")
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
        
        #Refresh
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/button').click()
        sleep(1)
        #drop down list num items
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]').click()
        sleep(1)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/ul/li[3]').click()
        numitemstext = driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/button/span[1]').text
        if (numitemstext == "50"):
            rst = True
        else:
            rst = False
        return rst
    def test_drop_down_list_num_50(self):
        result = self.check_drop_down_list_num_50()
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
        
    def check_drop_down_list_num_all(self):
        sreach_window = self.driver.current_window_handle
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys("j")
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
        
        #Refresh
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/button').click()
        sleep(1)
        #drop down list num items
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]').click()
        sleep(1)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/ul/li[4]').click()
        numitemstext = driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[1]/button/span[1]').text
        if (numitemstext == "All"):
            rst = True
        else:
            rst = False
        return rst
    def test_drop_down_list_num_all(self):
        result = self.check_drop_down_list_num_all()
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
        
                
    def check_add_app_page(self):
            
        #list down list descr item        
        self.driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[2]').click() 
        sleep(1)
        list_dsc_items = self.driver.find_elements_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[2]/ul/li')
        for j in list_dsc_items:
            sleep(1)
            j.click()
        #    driver.find_element_by_xpath('//*[@id="grid-data-header"]/div/div/div[2]/div[2]').click()
            sleep(1)
            j.click()            
        
        # 如果知道CheckBox的状态就知道是几个描述
        #lisID/AppName...
        text_id = self.driver.find_element_by_xpath('//*[@id="grid-data"]/thead/tr/th[1]/a/span[1]').text 
        print(text_id)
        text_appname = self.driver.find_element_by_xpath('//*[@id="grid-data"]/thead/tr/th[2]/a/span[1]').text
        print(text_appname)
        
        #The List num
        list_nums = self.driver.find_elements_by_xpath('//*[@id="grid-data"]/tbody/tr')
        i=0
        for list_num in list_nums:
            i= i+1
        print(i)
        
        sreach_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//*[@id="grid-data"]/tbody/tr/td[4]/button').click()
        sleep(1)
        sreach_window = self.driver.current_window_handle 
        print("Current title is %s"%self.driver.title) 
        print("Current url is %s"%self.driver.current_url)
        #addpageurl = 'http://10.110.1.55:8082/admin/apkinfo.html?id=0000-ad2238f9-4a4b-44ab-b3be-2c2ba46cb05f&status=1'
        if (self.driver.current_url.endswith('status=1')):
            rst = True
        else:
            rst = False
        return rst
    
    def test_check_add_app_page(self):
        result = self.check_add_app_page()
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
    
    def check_add_app_suggestion_title(self):
        sreach_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//*[@id="grid-data"]/tbody/tr/td[4]/button').click()
        sleep(1)
        sreach_window= self.driver.current_window_handle    
        self.driver.find_element_by_link_text('审核').click()    
        print("current suggest title %r"%self.driver.title)
        print("current suggest url %r"%self.driver.current_url)
        suggst_txt_title =  u'app store\u7ba1\u7406\u63a7\u5236\u53f0'
        if (suggst_txt_title == self.driver.title):
            rst = True
        else:
            rst = False
        return rst
    
    def test_add_app_suggestion(self):
        result = self.check_add_app_suggestion_title()
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
       
    def check_add_app_suggestion_submit(self):
        sreach_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//*[@id="grid-data"]/tbody/tr/td[4]/button').click()
        sleep(1)
        sreach_window= self.driver.current_window_handle    
        self.driver.find_element_by_link_text('审核').click() 
        sleep(1)
        sreach_window= self.driver.current_window_handle 
        self.driver.find_element_by_css_selector('span.bootstrap-switch-handle-on.bootstrap-switch-success').click()
        sleep(1)        
        #self.driver.find_element_by_css_selector('span.bootstrap-switch-handle-off.bootstrap-switch-warning').click()
            
        self.driver.find_element_by_id('reason').send_keys("suggestion")
        sleep(1)
        #driver.find_element_by_css_selector('button.btn.btn-default').click()
        sleep(1)
        self.driver.find_element_by_id('auditBtn').click()
        sleep(1)
        alert_text = self.driver.switch_to_alert().text
        print(alert_text)
        sleep(1)
        self.driver.switch_to_alert().accept()
        sleep(1)
        sreach_window= self.driver.current_window_handle 
        after_suggestion_submit_url = 'http://10.110.1.55:8082/admin/apkpendinglist.html'
        
        #if (alert_text == '保存成功'):
        #    rst = True
        #else:
        #    rst = False
        #print("alert_text %r"%rst)
        
        if(self.driver.current_url == after_suggestion_submit_url):
            rst = True
        else:
            rst = False
        return rst
        

    def test_add_app_suggestion_submit(self):
       result = self.check_add_app_suggestion_submit() 
       self.assertTrue(result)
       os.system("taskkill /F /IM firefox.exe")
    
    
if __name__ == '__main__':
    unittest.main()
