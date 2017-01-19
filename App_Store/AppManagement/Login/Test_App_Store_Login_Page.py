# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep
from App_Store_Login_Page import *

class TestAppStoreLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://10.110.1.55:8082/admin/home.html'
        #http://10.110.1.55:8082/login.html
        self.driver.get(self.base_url)
        sleep(1)
        
    def test_app_store_login_page(self):
        self.assertTrue(check_is_login_page)
        self.assertTrue(check_is_login_text_exist)
        self.assertTrue(check_is_login_username_icon_exist)
        self.assertTrue(check_is_login_password_icon_exist)
        self.assertTrue(check_is_username_frame_exist)
        self.assertTrue(check_is_password_frame_exist)
        self.assertTrue(check_is_login_button_exist)

if __name__ == '__main__':
    unittest.main()   
    
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()