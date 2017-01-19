# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep

class TestAppCategoryAddPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://10.110.1.55:8082/admin/home.html"
        #http://10.110.1.55:8082/login.html
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@value='登录']").click()
        sleep(1) 
        sreach_window=self.driver.current_window_handle    
        self.driver.find_element_by_link_text("应用分类").click()
        sleep(1)
        sreach_window=self.driver.current_window_handle
        
    def check_is_category_add_page(self):
        self.driver.find_element_by_link_text('添加分类').click()
        sleep(1) 
        sreach_window=self.driver.current_window_handle
        add_category_url = r"http://10.110.1.55:8082/admin/catnew.html"           
        print("Current add category page url is %r"%self.driver.current_url)
        if(add_category_url == self.driver.current_url):
            rst = True
        else:
            rst = False
        return rst
    
    def check_is_category_frame_exist(self, xpath_url):
        sreach_window=self.driver.current_window_handle
        if self.driver.find_element_by_xpath(xpath_url):
            rst = True
        else:
            rst = False
        return rst

    
    def check_is_category_add_text_exist(self, xpath_url, dest_text):
        sreach_window=self.driver.current_window_handle
        src_text = self.driver.find_element_by_xpath(xpath_url).text
        if(dest_text == src_text):
            rst = True
        else:
            rst = False
        return rst
             
    def test_is_category_add_page(self):         
        self.assertTrue(self.check_is_category_add_page())
        self.assertTrue(self.check_is_category_add_text_exist('//*[@id="catForm"]/div[1]/label', u'所属分类'))
        self.assertTrue(self.check_is_category_add_text_exist('//*[@id="catForm"]/div[2]/label', u'名称'))
        self.assertTrue(self.check_is_category_add_text_exist('//*[@id="catForm"]/div[3]/label', u'顺序'))
        self.assertTrue(self.check_is_category_add_text_exist('//*[@id="catForm"]/div[4]/label', u'图像'))
        self.assertTrue(self.check_is_category_frame_exist('//*[@id="parent"]'))
        self.assertTrue(self.check_is_category_frame_exist('//*[@id="catName"]'))
        self.assertTrue(self.check_is_category_frame_exist('//*[@id="seqNum"]'))
        self.assertTrue(self.check_is_category_frame_exist('//*[@id="dndArea"]'))
        self.assertTrue(self.check_is_category_frame_exist('//*[@id="catForm"]/div[4]/div/div[2]'))
        self.assertTrue(self.check_is_category_frame_exist('//*[@id="catForm"]/div[5]/div'))
        os.system("taskkill /F /IM firefox.exe")
        
        
        
        
if __name__ == '__main__':
  unittest.main()