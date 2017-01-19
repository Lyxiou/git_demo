# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep
import os
import sys
import signal

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://10.110.1.55:8082/admin/home.html"
        #目前这个网址http://10.110.1.55:8082/login.html有问题
        
    def login_check(self, username, password):
        self.driver.get(self.base_url)
        print("Current url is %s"%self.driver.current_url)
        print("Current title is %s"%self.driver.title)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_xpath("//input[@value='登录']").click() 
        sleep(3)
        print("Current url is %s"%self.driver.current_url)  
        print("Current title is %s"%self.driver.title) 
        sreach_window=self.driver.current_window_handle     
        print("Current title is %s"%self.driver.title) 
        main_page_url = 'http://10.110.1.55:8082/admin/home.html'
        if(main_page_url == self.driver.current_url):           
            rst = True
        else:
            rst = False   
        return rst
        
    def test_Login_success_with_right_u_p(self):
        result = self.login_check("admin", "123456")
        self.assertTrue(result)
        os.system("taskkill /F /IM firefox.exe")
           
    def test_login_fail_with_wrong_u_p(self):
        result = self.login_check("admin", "password")
        self.assertFalse(result) 
        os.system("taskkill /F /IM firefox.exe")     

if __name__ == '__main__':
    unittest.main()
